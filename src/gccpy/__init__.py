import subprocess

from .utils import lookup_files, change_file_extention
from .exceptions import DirectoryNotFoundError
from .conf import *


# Check for unfound direcotries.
if not CODE_DIR.exists():
    raise DirectoryNotFoundError(CODE_DIR.name, REPO_DIR.name)

if not INCLUDE_DIR.exists():
    raise DirectoryNotFoundError(INCLUDE_DIR.name, REPO_DIR.name)

# Make output directories.
if not BUILD_DIR.exists():
    BUILD_DIR.mkdir(exist_ok=True)

if not OBJECTS_DIR.exists():
    OBJECTS_DIR.mkdir(exist_ok=True)


__CFILES: list[Path] = lookup_files(CODE_DIR.name, ".c")
__OBJFILES: list[Path] = [OBJECTS_DIR / change_file_extention(str(cfile), ".o") for cfile in __CFILES]


def run_cmd(cmd: str):
    subprocess.run(cmd, shell=True, check=True)
