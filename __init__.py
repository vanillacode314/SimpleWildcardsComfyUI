"""
@author: VanillaCode314
@title: Simple Wildcard
@nickname: Simple Wildcard
@description: A simple wildcard node for ComfyUI. Can also be used a style prompt node.
"""

from .wildcard import Wildcard

NODE_CLASS_MAPPINGS = {"SimpleWildcard": Wildcard}
NODE_DISPLAY_NAME_MAPPINGS = {"SimpleWildcard": "SimpleWildcard"}
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
