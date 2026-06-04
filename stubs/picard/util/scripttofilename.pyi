from _typeshed import Incomplete
from picard.config import get_config as get_config
from picard.const.sys import IS_WIN as IS_WIN
from picard.metadata import Metadata as Metadata
from picard.script import ScriptParser as ScriptParser
from picard.util import (
    replace_win32_incompat as replace_win32_incompat,
    sanitize_filename as sanitize_filename,
)
from picard.util.textencoding import replace_non_ascii as replace_non_ascii

def script_to_filename_with_metadata(
    naming_format,
    metadata,
    file: Incomplete | None = None,
    settings: Incomplete | None = None,
): ...
def script_to_filename(
    naming_format,
    metadata,
    file: Incomplete | None = None,
    settings: Incomplete | None = None,
): ...
