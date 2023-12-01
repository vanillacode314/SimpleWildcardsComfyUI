import shutil
from pathlib import Path
import os

module_js_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "js")
application_root_directory = Path(__file__).parent.parent
application_web_extensions_directory = os.path.join(
    application_root_directory, "web", "extensions", "vanilla.simple.wildcard"
)

shutil.copytree(
    module_js_directory, application_web_extensions_directory, dirs_exist_ok=True
)
