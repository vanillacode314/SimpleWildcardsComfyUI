"""
@author: VanillaCode314
@title: Simple Wildcard
@nickname: Simple Wildcard
@description: A simple wildcard node for ComfyUI. Can also be used a style prompt node.
"""

from .wildcard import Wildcard
import sys
import os
import folder_paths

sys.path.append(os.path.dirname(__file__))

module_js_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "js")
application_root_directory = os.path.dirname(folder_paths.__file__)
application_web_extensions_directory = os.path.join(
    application_root_directory, "web", "extensions", "vanilla.simple.wildcard"
)

NODE_CLASS_MAPPINGS = {"SimpleWildcard": Wildcard}
NODE_DISPLAY_NAME_MAPPINGS = {"SimpleWildcard": "SimpleWildcard"}
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
