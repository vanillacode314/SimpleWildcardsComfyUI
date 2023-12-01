from pipe import where, map, dedup, sort
from .utils import flat_map
from pathlib import Path, PosixPath
import os
import folder_paths
import random

application_root_directory = os.path.dirname(folder_paths.__file__)
wildcards_directory = Path(application_root_directory) / "wildcards"
if not wildcards_directory.is_dir():
    wildcards_directory.mkdir()
files = list(
    wildcards_directory.glob("**/*.txt")
    | map(lambda x: x.relative_to(wildcards_directory))
)


def get_items_for_wildcard_path(glob: str):
    return list(
        wildcards_directory.glob(glob)
        | where(lambda path: path.is_file())
        | flat_map(lambda path: path.read_text("utf-8").splitlines())
        | dedup
    )


class Wildcard:
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
                "seed": ("INT", {}),
                "input_files": (input_files, {"default": input_files[0]}),
                "input_text": (["*"] + items, {"default": "*"}),
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
        items = get_items_for_wildcard_path(kwargs["input_files"])
        output_text = kwargs["input_text"]
        if kwargs["input_text"] == "*":
            random.seed(kwargs["seed"])
            output_text = random.choice(items)

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
