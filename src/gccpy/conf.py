from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent

BUILD_DIR = BASE_DIR / "build"
"""where binaries will be stored."""

BINARY = BUILD_DIR / "bin"
"""Defualt binary name."""

CODE_DIRS: Path | list[Path] = BASE_DIR / "src"
"""Main dir to look for source files."""

INCLUDE_DIRS: Path | list[Path] = BASE_DIR / "include"
"""Main dir to look for header files."""

LIB_DIR: Path = BASE_DIR / "lib"
"""Main dir to look for libraries."""

OBJECTS_DIR: Path = BUILD_DIR / "objects"
"""Where output objects will be stored."""

DEPENDENCY_DIR: Path = BUILD_DIR / "deps"
"""Where output objects will be stored."""
