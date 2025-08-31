from pathlib import Path


REPO_DIR = Path(__file__).resolve().parent.parent.parent

BUILD_DIR = REPO_DIR / "build"
"""where binaries will be stored."""

BINARY = "bin"
"""Defualt binary name."""

BINARY_PATH = BUILD_DIR / BINARY
"""Defualt binary path."""

CODE_DIR = REPO_DIR / "src"
"""Main dir to look for source files."""

INCLUDE_DIR = REPO_DIR / "include"
"""Main dir to look for header files."""

OBJECTS_DIR = REPO_DIR / "objects"
"""Where output objects will be stored."""


CC = "gcc"
"""C compiler name."""

STD = "c2x"
"""C standard to use."""

OPTIONS = "-g -c"
"""General Options."""

OPTIMIZATION_OPTIONS = "-O0"
"""Optimization flags."""

DEPENDENCY_OPTIONS = ""
"""Dependency flags."""

WARNING_OPTIONS = "-Wall -Wextra"
"""General Warning options."""

CFLAGS = f"--std={STD} {WARNING_OPTIONS} {OPTIONS} {OPTIMIZATION_OPTIONS} -I{INCLUDE_DIR} {DEPENDENCY_OPTIONS}"
"""Compined C flags."""
