from _typeshed import Incomplete
from picard import log as log
from picard.config import get_config as get_config
from picard.coverart.image import (
    CoverArtImageError as CoverArtImageError,
    TagCoverArtImage as TagCoverArtImage,
)
from picard.file import File as File
from picard.formats.mutagenext import delall_ci as delall_ci
from picard.metadata import Metadata as Metadata
from picard.util import encode_filename as encode_filename

UNSUPPORTED_TAGS: Incomplete

class MP4File(File):
    EXTENSIONS: Incomplete
    NAME: str
    def __init__(self, filename) -> None: ...
    @classmethod
    def supports_tag(cls, name): ...
