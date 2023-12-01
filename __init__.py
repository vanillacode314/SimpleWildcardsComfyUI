"""
@author: VanillaCode314
@title: Simple Wildcard
@nickname: Simple Wildcard
@description: A simple wildcard node for ComfyUI. Can also be used a style prompt node.
"""

import os


def do_install():
    import importlib

    spec = importlib.util.spec_from_file_location(
        "simple_install", os.path.join(os.path.dirname(__file__), "install.py")
    )
    simple_install = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(simple_install)


do_install()

from .wildcard import SimpleWildcard
from .concat import SimpleConcat


NODE_CLASS_MAPPINGS = {"SimpleWildcard": SimpleWildcard, "SimpleConcat": SimpleConcat}
NODE_DISPLAY_NAME_MAPPINGS = {
    "SimpleWildcard": "SimpleWildcard",
    "SimpleConcat": "SimpleConcat",
}
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
