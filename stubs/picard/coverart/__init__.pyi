from _typeshed import Incomplete
from picard import log as log
from picard.config import get_config as get_config
from picard.coverart.image import (
    CoverArtImageIOError as CoverArtImageIOError,
    CoverArtImageIdentificationError as CoverArtImageIdentificationError,
)
from picard.coverart.providers import (
    CoverArtProvider as CoverArtProvider,
    cover_art_providers as cover_art_providers,
)
from picard.metadata import (
    register_album_metadata_processor as register_album_metadata_processor,
)

class CoverArt:
    album: Incomplete
    metadata: Incomplete
    release: Incomplete
    front_image_found: bool
    def __init__(self, album, metadata, release) -> None: ...
    providers: Incomplete
    def retrieve(self) -> None: ...
    def next_in_queue(self) -> None: ...
    def queue_put(self, coverartimage) -> None: ...
