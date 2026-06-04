from _typeshed import Incomplete
from picard import log as log
from picard.config import get_config as get_config
from picard.coverart.image import (
    CoverArtImageError as CoverArtImageError,
    TagCoverArtImage as TagCoverArtImage,
)
from picard.coverart.utils import types_from_id3 as types_from_id3
from picard.file import File as File
from picard.formats.util import guess_format as guess_format
from picard.metadata import Metadata as Metadata
from picard.util import (
    encode_filename as encode_filename,
    sanitize_date as sanitize_date,
)

FLAC_MAX_BLOCK_SIZE: Incomplete
INVALID_CHARS: Incomplete
UNSUPPORTED_TAGS: Incomplete

def sanitize_key(key): ...
def is_valid_key(key): ...
def flac_sort_pics_after_tags(metadata_blocks) -> None: ...
def flac_remove_empty_seektable(file) -> None: ...

class VCommentFile(File):
    @classmethod
    def supports_tag(cls, name): ...

class FLACFile(VCommentFile):
    EXTENSIONS: Incomplete
    NAME: str

class OggFLACFile(VCommentFile):
    EXTENSIONS: Incomplete
    NAME: str

class OggSpeexFile(VCommentFile):
    EXTENSIONS: Incomplete
    NAME: str

class OggTheoraFile(VCommentFile):
    EXTENSIONS: Incomplete
    NAME: str

class OggVorbisFile(VCommentFile):
    EXTENSIONS: Incomplete
    NAME: str

class OggOpusFile(VCommentFile):
    EXTENSIONS: Incomplete
    NAME: str
    @classmethod
    def supports_tag(cls, name): ...

def OggAudioFile(filename): ...
def OggVideoFile(filename): ...
def OggContainerFile(filename): ...
