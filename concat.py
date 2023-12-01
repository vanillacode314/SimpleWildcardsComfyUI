class SimpleConcat:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "num": ("INT", {"default": 2, "min": 2, "max": 10}),
                "delimeter": ("STRING", {"default": ", ", "dynamicPrompts": False}),
                "output_text": (
                    "STRING",
                    {"multiline": True, "dynamicPrompts": False, "default": ""},
                ),
            },
            "optional": {
                "input_0": (
                    "STRING",
                    {"default": "", "dynamicPrompts": False, "multiline": True},
                ),
                "input_1": (
                    "STRING",
                    {"default": "", "dynamicPrompts": False, "multiline": True},
                ),
                "input_2": (
                    "STRING",
                    {"default": "", "dynamicPrompts": False, "multiline": True},
                ),
                "input_3": (
                    "STRING",
                    {"default": "", "dynamicPrompts": False, "multiline": True},
                ),
                "input_4": (
                    "STRING",
                    {"default": "", "dynamicPrompts": False, "multiline": True},
                ),
                "input_5": (
                    "STRING",
                    {"default": "", "dynamicPrompts": False, "multiline": True},
                ),
                "input_6": (
                    "STRING",
                    {"default": "", "dynamicPrompts": False, "multiline": True},
                ),
                "input_7": (
                    "STRING",
                    {"default": "", "dynamicPrompts": False, "multiline": True},
                ),
                "input_8": (
                    "STRING",
                    {"default": "", "dynamicPrompts": False, "multiline": True},
                ),
                "input_9": (
                    "STRING",
                    {"default": "", "dynamicPrompts": False, "multiline": True},
                ),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "func"
    CATEGORY = "vanilla"
    OUTPUT_NODE = True

    def func(self, *args, **kwargs):
        output_text = kwargs["delimeter"].join(
            [
                value
                for key, value in kwargs.items()
                if key.startswith("input") and value.strip() != ""
            ]
        )
        return {
            "ui": {"output_text": output_text},
            "result": (output_text,),
        }
