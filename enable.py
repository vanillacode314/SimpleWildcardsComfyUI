import shutil
from pathlib import Path

module_js_directory = Path(__file__).parent / "js"
application_root_directory = Path(__file__).parent.parent

shutil.copytree(
    module_js_directory,
    application_root_directory / "web" / "extensions" / "vanilla.simple.wildcard",
    dirs_exist_ok=True,
)
