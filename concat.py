class SimpleConcat:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "delimeter": ("STRING", {"default": ", ", "dynamicPrompts": False}),
            },
            "optional": {
                "input_0": (
                    "STRING",
                    {
                        "forceInput": True,
                        "default": "",
                    },
                ),
                "input_1": (
                    "STRING",
                    {
                        "forceInput": True,
                        "default": "",
                    },
                ),
                "input_2": (
                    "STRING",
                    {
                        "forceInput": True,
                        "default": "",
                    },
                ),
                "input_3": (
                    "STRING",
                    {
                        "forceInput": True,
                        "default": "",
                    },
                ),
                "input_4": (
                    "STRING",
                    {
                        "forceInput": True,
                        "default": "",
                    },
                ),
                "input_5": (
                    "STRING",
                    {
                        "forceInput": True,
                        "default": "",
                    },
                ),
                "input_6": (
                    "STRING",
                    {
                        "forceInput": True,
                        "default": "",
                    },
                ),
                "input_7": (
                    "STRING",
                    {
                        "forceInput": True,
                        "default": "",
                    },
                ),
                "input_8": (
                    "STRING",
                    {
                        "forceInput": True,
                        "default": "",
                    },
                ),
                "input_9": (
                    "STRING",
                    {
                        "forceInput": True,
                        "default": "",
                    },
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
        output_text = kwargs["delimeter"].join(
            [
                value
                for key, value in kwargs.items()
                if key.startswith("input")
                and value.strip() != ""
                and value != None
                and value != "undefined"
                and value != "null"
            ]
        )
        return {
            "ui": {"output_text": output_text},
            "result": (output_text,),
        }
