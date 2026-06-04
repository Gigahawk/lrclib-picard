from _typeshed import Incomplete
from picard import log as log
from picard.config import get_config as get_config
from picard.const import DEFAULT_COVER_IMAGE_FILENAME as DEFAULT_COVER_IMAGE_FILENAME
from picard.const.sys import IS_MACOS as IS_MACOS, IS_WIN as IS_WIN
from picard.coverart.utils import (
    Id3ImageType as Id3ImageType,
    image_type_as_id3_num as image_type_as_id3_num,
    translate_caa_type as translate_caa_type,
)
from picard.metadata import Metadata as Metadata
from picard.util import (
    decode_filename as decode_filename,
    encode_filename as encode_filename,
    imageinfo as imageinfo,
    is_absolute_path as is_absolute_path,
    periodictouch as periodictouch,
    sanitize_filename as sanitize_filename,
)
from picard.util.filenaming import (
    make_save_path as make_save_path,
    make_short_filename as make_short_filename,
)
from picard.util.scripttofilename import script_to_filename as script_to_filename

class DataHash:
    def __init__(self, data, prefix: str = "picard", suffix: str = "") -> None: ...
    def __eq__(self, other): ...
    def hash(self): ...
    def delete_file(self) -> None: ...
    @property
    def data(self): ...
    @property
    def filename(self): ...

class CoverArtImageError(Exception): ...
class CoverArtImageIOError(CoverArtImageError): ...
class CoverArtImageIdentificationError(CoverArtImageError): ...

class CoverArtImage:
    support_types: bool
    support_multi_types: bool
    is_front: Incomplete
    sourceprefix: str
    types: Incomplete
    url: Incomplete
    comment: Incomplete
    datahash: Incomplete
    thumbnail: Incomplete
    can_be_saved_to_tags: bool
    can_be_saved_to_disk: bool
    can_be_saved_to_metadata: bool
    def __init__(
        self,
        url: Incomplete | None = None,
        types: Incomplete | None = None,
        comment: str = "",
        data: Incomplete | None = None,
        support_types: Incomplete | None = None,
        support_multi_types: Incomplete | None = None,
        id3_type: Incomplete | None = None,
    ) -> None: ...
    @property
    def source(self): ...
    def is_front_image(self): ...
    def imageinfo_as_string(self): ...
    def __eq__(self, other): ...
    def __hash__(self): ...
    def set_data(self, data) -> None: ...
    @property
    def maintype(self): ...
    @property
    def id3_type(self): ...
    @id3_type.setter
    def id3_type(self, type) -> None: ...
    def save(self, dirname, metadata, counters) -> None: ...
    @property
    def data(self): ...
    @property
    def tempfile_filename(self): ...
    def normalized_types(self): ...
    def types_as_string(self, translate: bool = True, separator: str = ", "): ...

class CaaCoverArtImage(CoverArtImage):
    support_types: bool
    support_multi_types: bool
    sourceprefix: str
    is_front: Incomplete
    def __init__(
        self,
        url,
        types: Incomplete | None = None,
        is_front: bool = False,
        comment: str = "",
        data: Incomplete | None = None,
    ) -> None: ...

class CaaThumbnailCoverArtImage(CaaCoverArtImage):
    is_front: bool
    can_be_saved_to_disk: bool
    can_be_saved_to_tags: bool
    can_be_saved_to_metadata: bool
    def __init__(
        self,
        url,
        types: Incomplete | None = None,
        is_front: bool = False,
        comment: str = "",
        data: Incomplete | None = None,
    ) -> None: ...

class TagCoverArtImage(CoverArtImage):
    sourcefile: Incomplete
    tag: Incomplete
    support_types: Incomplete
    support_multi_types: Incomplete
    is_front: Incomplete
    def __init__(
        self,
        file,
        tag: Incomplete | None = None,
        types: Incomplete | None = None,
        is_front: Incomplete | None = None,
        support_types: bool = False,
        comment: str = "",
        data: Incomplete | None = None,
        support_multi_types: bool = False,
        id3_type: Incomplete | None = None,
    ) -> None: ...
    @property
    def source(self): ...

class LocalFileCoverArtImage(CoverArtImage):
    sourceprefix: str
    support_types: Incomplete
    support_multi_types: Incomplete
    def __init__(
        self,
        filepath,
        types: Incomplete | None = None,
        comment: str = "",
        support_types: bool = False,
        support_multi_types: bool = False,
    ) -> None: ...
