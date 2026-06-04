from _typeshed import Incomplete
from enum import IntEnum
from picard import log as log
from picard.const.sys import (
    IS_LINUX as IS_LINUX,
    IS_MACOS as IS_MACOS,
    IS_WIN as IS_WIN,
)
from picard.util import (
    WIN_MAX_DIRPATH_LEN as WIN_MAX_DIRPATH_LEN,
    WIN_MAX_FILEPATH_LEN as WIN_MAX_FILEPATH_LEN,
    WIN_MAX_NODE_LEN as WIN_MAX_NODE_LEN,
    decode_filename as decode_filename,
    encode_filename as encode_filename,
    samefile as samefile,
)

win32api: Incomplete

class ShortenMode(IntEnum):
    BYTES = 0
    UTF16 = 1
    UTF16_NFD = 2

def shorten_filename(filename, length, mode): ...
def shorten_path(path, length, mode): ...

class WinPathTooLong(OSError): ...

def make_short_filename(
    basedir, relpath, win_shorten_path: bool = False, relative_to: str = ""
): ...
def samefile_different_casing(path1, path2): ...
def move_ensure_casing(source_path, target_path) -> None: ...
def make_save_path(path, win_compat: bool = False, mac_compat: bool = False): ...
def get_available_filename(new_path, old_path: Incomplete | None = None): ...
def replace_extension(filename, new_ext): ...
