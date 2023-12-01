class SimpleConcat:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "delimeter": ("STRING", {"default": ", ", "dynamicPrompts": False}),
                "output_text": (
                    "STRING",
                    {"multiline": True, "dynamicPrompts": False, "default": ""},
                ),
            },
            "optional": {
                "input_0": (
                    "STRING",
                    {
                        "forceInput": True,
                        "default": "",
                        "multiline": True,
                    },
                ),
                "input_1": (
                    "STRING",
                    {
                        "forceInput": True,
                        "default": "",
                        "multiline": True,
                    },
                ),
                "input_2": (
                    "STRING",
                    {
                        "forceInput": True,
                        "default": "",
                        "multiline": True,
                    },
                ),
                "input_3": (
                    "STRING",
                    {
                        "forceInput": True,
                        "default": "",
                        "multiline": True,
                    },
                ),
                "input_4": (
                    "STRING",
                    {
                        "forceInput": True,
                        "default": "",
                        "multiline": True,
                    },
                ),
                "input_5": (
                    "STRING",
                    {
                        "forceInput": True,
                        "default": "",
                        "multiline": True,
                    },
                ),
                "input_6": (
                    "STRING",
                    {
                        "forceInput": True,
                        "default": "",
                        "multiline": True,
                    },
                ),
                "input_7": (
                    "STRING",
                    {
                        "forceInput": True,
                        "default": "",
                        "multiline": True,
                    },
                ),
                "input_8": (
                    "STRING",
                    {
                        "forceInput": True,
                        "default": "",
                        "multiline": True,
                    },
                ),
                "input_9": (
                    "STRING",
                    {
                        "forceInput": True,
                        "default": "",
                        "multiline": True,
                    },
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
