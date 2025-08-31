from pathlib import Path
import os

from .exceptions import ExtentionStructureNotValid


def lookup_files(basedir: str, extention: str) -> list[Path]:
    """Searches for files with a specific extention."""
    found_files: list[Path] = []
    for root, _, files in Path(basedir).walk():
        for file in files:
            file_path = root / file
            if file_path.exists() and file_path.is_file() and file_path.name.endswith(extention):
                found_files.append(file_path)
    return found_files


def change_file_extention(filename: str, extention: str) -> str:
    """Changes the file extention."""
    # check for valid extention structure.
    if not extention.startswith('.'):
        raise ExtentionStructureNotValid("Extention must start with a `.`")
    return "".join(os.path.splitext(filename)[:-1]) + extention
