from pathlib import Path
import shutil

root_directory = Path(__file__).parent
module_js_directory = root_directory / "js"
application_root_directory = Path(__file__).parent.parent.parent

shutil.rmtree(
    application_root_directory / "web" / "extensions" / "vanilla.simple.wildcard"
)
