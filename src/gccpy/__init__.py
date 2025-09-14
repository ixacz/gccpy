from dataclasses import dataclass, field
from enum import Enum, auto
from pathlib import Path
import subprocess


from .utils import lookup_files, change_file_extention, path_shorter, run
from .exceptions import DirectoryNotFoundError
from .conf import *

BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent

# Check for unfound direcotries.
if not CODE_DIRS.exists():
    raise DirectoryNotFoundError(CODE_DIRS.name, BASE_DIR.name)

if not INCLUDE_DIRS.exists():
    raise DirectoryNotFoundError(INCLUDE_DIRS.name, BASE_DIR.name)

# Make output directories.
if not BUILD_DIR.exists():
    BUILD_DIR.mkdir(exist_ok=True)

if not OBJECTS_DIR.exists():
    OBJECTS_DIR.mkdir(exist_ok=True)

if not DEPENDENCY_DIR.exists():
    DEPENDENCY_DIR.mkdir(exist_ok=True)


class BuildType(Enum):
    BINARY = auto()
    LIBRARY = auto()


class LibType(Enum):
    SOURCE = auto()
    STATIC = auto()
    SHARED = auto()


@dataclass
class Lib:
    path: Path
    type: LibType


def get_lib(path: Path, type: LibType) -> Lib:
    return Lib(path, type)


@dataclass
class CFlags:
    compiler: str = field(default="gcc")
    std: str = field(default="c2x")
    options: str = field(default="-g -c")
    warnings: str = field(default="-Wall -Wextra")
    dependencies: str = field(default="")
    optimizations: str = field(default="-O0")

    def get_cflags(self) -> str:
        return f"{self.compiler} {self.std} {self.options} {self.warnings} {self.dependencies} {self.optimizations}"


def compile_binary(cflags: CFlags) -> None:
    cdirs_by_files: dict[Path, list[Path]] = {}
    if isinstance(CODE_DIRS, list):
        for code_dir in CODE_DIRS:
            cdirs_by_files += {code_dir: lookup_files(code_dir, ".c")}
    else:
        cdirs_by_files = {code_dir: lookup_files(CODE_DIRS, ".c")}

    for cdir, cfiles in cdirs_by_files.items():
        for cfile in cfiles:
            objfile = OBJECTS_DIR / change_file_extention(
                path_shorter(str(cfile), str(cdir)),
                ".o"
            )
            cflags = f"{cflags.compiler} {cflags.std} {cflags.options} {cflags.warnings} {cflags.dependencies} {cflags.optimizations}"

def compile_library(cflags: CFlags) -> None:
    pass


def project(
    name: str | None,
    type: BuildType | None,
    cflags: CFlags | None
):
    # define defualts
    name: str = name or BASE_DIR.name
    type: BuildType = type or BuildType.BINARY
    cflags: CFlags = cflags or CFlags()

    match type:
        case BuildType.BINARY:
            compile_binary(cflags)

        case BuildType.LIBRARY:
            compile_library(cflags)
