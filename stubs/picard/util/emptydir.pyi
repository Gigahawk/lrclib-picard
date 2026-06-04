from _typeshed import Incomplete
from picard.util import get_qt_enum as get_qt_enum

JUNK_FILES: Incomplete
PROTECTED_DIRECTORIES: Incomplete
value: Incomplete

class SkipRemoveDir(Exception): ...

def is_empty_dir(path, ignored_files: Incomplete | None = None): ...
def rm_empty_dir(path) -> None: ...
