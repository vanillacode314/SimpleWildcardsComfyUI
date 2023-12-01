import shutil
from .vars import module_js_directory, application_root_directory

shutil.copytree(
    module_js_directory,
    application_root_directory / "web" / "extensions" / "vanilla.simple.wildcard",
    dirs_exist_ok=True,
)
