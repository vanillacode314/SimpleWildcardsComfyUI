from pipe import where, map, dedup, sort
from .utils import flat_map
from pathlib import Path
from .vars import application_root_directory
import re, random
import functools

wildcards_directory = application_root_directory / "wildcards"
if not wildcards_directory.is_dir():
    wildcards_directory.mkdir()
files = list(
    wildcards_directory.glob("**/*.txt")
    | map(lambda x: x.relative_to(wildcards_directory))
)
item_map = dict()


@functools.lru_cache()
def get_items_for_wildcard_path(glob: str, regex: str = ".*", exclude_regex: str = ""):
    return list(
        wildcards_directory.glob(glob)
        | where(lambda path: path.is_file())
        | flat_map(lambda path: path.read_text("utf-8").splitlines())
        | dedup
        | where(
            lambda x: re.search(regex, x, re.IGNORECASE)
            and (exclude_regex == "" or not re.search(exclude_regex, x, re.IGNORECASE))
        )
    )


class SimpleWildcard:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        def map_names(path: Path) -> list[str]:
            output: list[str] = []
            path_str = path.as_posix()
            output.append(path_str)
            if path_str.count("/") > 0:
                base = path_str[: path_str.index("/")]
                output.append(f"{base}/*.txt")
                output.append(f"{base}/**/*.txt")
            return output

        input_files = files | flat_map(map_names) | dedup | sort
        items = get_items_for_wildcard_path("**/*.txt")

        return {
            "required": {
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xFFFFFFFFFFFFFFFF}),
                "input_files": (input_files, {"default": input_files[0]}),
                "input_text": (["*"] + items, {"default": "*"}),
                "weight": (
                    "FLOAT",
                    {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.1},
                ),
                "prefix": ("STRING", {"default": "", "dynamicPrompts": False}),
                "suffix": ("STRING", {"default": "", "dynamicPrompts": False}),
                "regex": (
                    "STRING",
                    {"default": ".*"},
                ),
                "exclude_regex": (
                    "STRING",
                    {"default": ""},
                ),
                "temp_override": (
                    "STRING",
                    {"default": ""},
                ),
                "output_blank_ratio": (
                    "FLOAT",
                    {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.05},
                ),
                "output_text": (
                    "STRING",
                    {"multiline": True, "dynamicPrompts": False, "default": ""},
                ),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "func"
    CATEGORY = "vanilla"
    OUTPUT_NODE = True

    def func(self, *args, **kwargs):
        wildcard_mode_enabled = kwargs["input_text"] == "*"
        should_apply_weight = kwargs["weight"] != 1

        if kwargs["temp_override"] != "":
            output_text = f"{kwargs['prefix']} {kwargs['temp_override']} {kwargs['suffix']}".strip()

            if should_apply_weight:
                output_text = f"({output_text}:{round(kwargs['weight'], 2)})"
            return {
                "ui": {"output_text": output_text},
                "result": (output_text,),
            }

        rng = random.Random(kwargs["seed"])
        if rng.random() < kwargs["output_blank_ratio"]:
            return {
                "ui": {"output_text": ""},
                "result": ("",),
            }

        output_text = kwargs["input_text"]

        if wildcard_mode_enabled:
            items = get_items_for_wildcard_path(
                kwargs["input_files"], kwargs["regex"], kwargs["exclude_regex"]
            )
            has_items = len(items) > 0
            if has_items:
                output_text = rng.choice(items)
            else:
                output_text = ""

        output_text = f"{kwargs['prefix']} {output_text} {kwargs['suffix']}".strip()

        if should_apply_weight:
            output_text = f"({output_text}:{round(kwargs['weight'], 2)})"

        return {
            "ui": {"output_text": output_text},
            "result": (output_text,),
        }


from server import PromptServer
from aiohttp import web


@PromptServer.instance.routes.get("/simple-wildcards")
async def my_hander_method(request):
    path = request._rel_url.query["path"]
    return web.json_response({"items": ["*"] + get_items_for_wildcard_path(path)})
