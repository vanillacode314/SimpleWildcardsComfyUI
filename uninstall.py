import shutil
from .vars import application_root_directory

shutil.rmtree(
    application_root_directory / "web" / "extensions" / "vanilla.simple.wildcard"
)
