
class DirectoryNotFoundError(Exception):
    """Directory not found exception."""
    def __init__(self, dir_name: str, at: str):
        msg = f"{dir_name} was not found."
        super().__init__(msg)


class ExtentionStructureNotValid(Exception):
    """Extention has an invalid structure."""
    def __init__(self, msg: str,):
        super().__init__(msg)
