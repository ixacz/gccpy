from pathlib import Path
import subprocess
import os

from .exceptions import ExtentionStructureNotValid

import yaml


def load_gccpy_config_file() -> dict:
    """Loads the config file `gccpy.yaml`."""
    path = Path(__file__).resolve().parent / "gccpy.yaml"

    try:
        with open(path, 'r') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        raise FileNotFoundError("Please make sure you configure `gccpy.yaml` file before running the build.")

def lookup_files(basedir: Path, extention: str) -> list[Path]:
    """Searches for files with a specific extention."""
    found_files: list[Path] = []
    for root, _, files in basedir.walk():
        for file in files:
            file_path = root / file
            if file_path.exists() and file_path.is_file() and file_path.name.endswith(extention):
                found_files.append(file_path)
    return found_files

def path_shorter(path: str, _from: str) -> str:
    path = path.split('/')
    from_idx = path.index(_from)
    return "/".join(path[from_idx:])

def change_file_extention(filename: str, extention: str) -> str:
    """Changes the file extention."""
    # check for valid extention structure.
    if not extention.startswith('.'):
        raise ExtentionStructureNotValid("Extention must start with a `.`")
    return "".join(os.path.splitext(filename)[:-1]) + extention

def run(cmd: str, echo: bool = True):
    """Runs a command in the shell."""
    if echo:
        print(cmd)
    subprocess.run(cmd, shell=True, check=True)
