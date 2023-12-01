from pathlib import Path
import shutil
import sys
import subprocess
import threading
import locale
import re
from vars import module_js_directory, application_root_directory, root_directory

if "python_embeded" in sys.executable or "python_embedded" in sys.executable:
    pip_install = [sys.executable, "-s", "-m", "pip", "install"]
else:
    pip_install = [sys.executable, "-m", "pip", "install"]


def handle_stream(stream, is_stdout):
    stream.reconfigure(encoding=locale.getpreferredencoding(), errors="replace")

    for msg in stream:
        if is_stdout:
            print(msg, end="", file=sys.stdout)
        else:
            print(msg, end="", file=sys.stderr)


def process_wrap(cmd_str, cwd=None, handler=None):
    print(f"[Simple Wildcard] EXECUTE: {cmd_str} in '{cwd}'")
    process = subprocess.Popen(
        cmd_str,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1,
    )

    if handler is None:
        handler = handle_stream

    stdout_thread = threading.Thread(target=handler, args=(process.stdout, True))
    stderr_thread = threading.Thread(target=handler, args=(process.stderr, False))

    stdout_thread.start()
    stderr_thread.start()

    stdout_thread.join()
    stderr_thread.join()

    return process.wait()


# ---


pip_list = None


def get_installed_packages():
    global pip_list

    if pip_list is None:
        try:
            result = subprocess.check_output(
                [sys.executable, "-m", "pip", "list"], universal_newlines=True
            )
            pip_list = set(
                [line.split()[0].lower() for line in result.split("\n") if line.strip()]
            )
        except subprocess.CalledProcessError as e:
            print(
                f"[Simple Wildcard] Failed to retrieve the information of installed pip packages."
            )
            return set()

    return pip_list


def is_installed(name):
    name = name.strip()
    pattern = r"([^<>!=]+)([<>!=]=?)"
    match = re.search(pattern, name)

    if match:
        name = match.group(1)

    result = name.lower() in get_installed_packages()
    return result


def is_requirements_installed(file_path: Path):
    print(f"req_path: {file_path.as_posix()}")
    if file_path.exists():
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                if not is_installed(line):
                    return False

    return True


requirements_path = root_directory / "requirements.txt"


def ensure_requirements_installed():
    if not is_requirements_installed(requirements_path):
        process_wrap(pip_install + ["-r", requirements_path])


if __name__ == "__main__":
    shutil.copytree(
        module_js_directory,
        application_root_directory / "web" / "extensions" / "vanilla.simple.wildcard",
        dirs_exist_ok=True,
    )
    ensure_requirements_installed()
