"""
@author: VanillaCode314
@title: Simple Wildcard
@nickname: Simple Wildcard
@description: A simple wildcard node for ComfyUI. Can also be used a style prompt node.
"""

from .wildcard import SimpleWildcard
from .concat import SimpleConcat

NODE_CLASS_MAPPINGS = {"SimpleWildcard": SimpleWildcard, "SimpleConcat": SimpleConcat}
NODE_DISPLAY_NAME_MAPPINGS = {
    "SimpleWildcard": "SimpleWildcard",
    "SimpleConcat": "SimpleConcat",
}
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
