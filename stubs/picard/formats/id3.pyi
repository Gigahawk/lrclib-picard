from _typeshed import Incomplete
from enum import IntEnum
from picard import log as log
from picard.config import get_config as get_config
from picard.coverart.image import (
    CoverArtImageError as CoverArtImageError,
    TagCoverArtImage as TagCoverArtImage,
)
from picard.coverart.utils import types_from_id3 as types_from_id3
from picard.file import File as File
from picard.formats.mutagenext import compatid3 as compatid3, delall_ci as delall_ci
from picard.metadata import Metadata as Metadata
from picard.util import (
    encode_filename as encode_filename,
    sanitize_date as sanitize_date,
)
from picard.util.tags import parse_comment_tag as parse_comment_tag

UNSUPPORTED_TAGS: Incomplete

class Id3Encoding(IntEnum):
    LATIN1 = 0
    UTF16 = 1
    UTF16BE = 2
    UTF8 = 3
    def from_config(id3v2_encoding): ...

def id3text(text, encoding): ...

class ID3File(File):
    def __init__(self, filename) -> None: ...
    def build_TXXX(self, encoding, desc, values): ...
    @classmethod
    def supports_tag(cls, name): ...
    def format_specific_metadata(
        self, metadata, tag, settings: Incomplete | None = None
    ): ...

class MP3File(ID3File):
    EXTENSIONS: Incomplete
    NAME: str

class TrueAudioFile(ID3File):
    EXTENSIONS: Incomplete
    NAME: str

class NonCompatID3File(ID3File): ...

class DSFFile(NonCompatID3File):
    EXTENSIONS: Incomplete
    NAME: str

class AiffFile(NonCompatID3File):
    EXTENSIONS: Incomplete
    NAME: str

class DSDIFFFile(NonCompatID3File):
    EXTENSIONS: Incomplete
    NAME: str
