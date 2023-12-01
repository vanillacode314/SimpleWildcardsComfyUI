import shutil
from . import application_web_extensions_directory, module_js_directory

shutil.copytree(
    module_js_directory, application_web_extensions_directory, dirs_exist_ok=True
)
