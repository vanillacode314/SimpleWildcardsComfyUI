"""
@author: VanillaCode314
@title: Simple Wildcard
@nickname: Simple Wildcard
@description: A simple wildcard node for ComfyUI. Can also be used a style prompt node.
"""

from .wildcard import Wildcard
from pathlib import Path
import os

module_js_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "js")
application_root_directory = Path(__file__).parent.parent
application_web_extensions_directory = os.path.join(
    application_root_directory, "web", "extensions", "vanilla.simple.wildcard"
)

NODE_CLASS_MAPPINGS = {"SimpleWildcard": Wildcard}
NODE_DISPLAY_NAME_MAPPINGS = {"SimpleWildcard": "SimpleWildcard"}
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
