from .mutagenext import aac as aac, tak as tak
from _typeshed import Incomplete
from picard import log as log
from picard.config import get_config as get_config
from picard.coverart.image import (
    CoverArtImageError as CoverArtImageError,
    TagCoverArtImage as TagCoverArtImage,
)
from picard.file import File as File
from picard.metadata import Metadata as Metadata
from picard.util import (
    encode_filename as encode_filename,
    sanitize_date as sanitize_date,
)
from picard.util.filenaming import (
    get_available_filename as get_available_filename,
    move_ensure_casing as move_ensure_casing,
    replace_extension as replace_extension,
)

INVALID_CHARS: Incomplete
DISALLOWED_KEYS: Incomplete
UNSUPPORTED_TAGS: Incomplete

def is_valid_key(key): ...

class APEv2File(File):
    def __init__(self, filename) -> None: ...
    @classmethod
    def supports_tag(cls, name): ...

class MusepackFile(APEv2File):
    EXTENSIONS: Incomplete
    NAME: str

class WavPackFile(APEv2File):
    EXTENSIONS: Incomplete
    NAME: str

class OptimFROGFile(APEv2File):
    EXTENSIONS: Incomplete
    NAME: str

class MonkeysAudioFile(APEv2File):
    EXTENSIONS: Incomplete
    NAME: str

class TAKFile(APEv2File):
    EXTENSIONS: Incomplete
    NAME: str

class AACFile(APEv2File):
    EXTENSIONS: Incomplete
    NAME: str
    @classmethod
    def supports_tag(cls, name): ...
