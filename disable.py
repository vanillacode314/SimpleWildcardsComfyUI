import shutil
from pathlib import Path

application_root_directory = Path(__file__).parent.parent
shutil.rmtree(
    application_root_directory / "web" / "extensions" / "vanilla.simple.wildcard"
)
