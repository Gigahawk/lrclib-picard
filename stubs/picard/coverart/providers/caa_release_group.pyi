from _typeshed import Incomplete
from picard.coverart.image import (
    CaaCoverArtImage as CaaCoverArtImage,
    CaaThumbnailCoverArtImage as CaaThumbnailCoverArtImage,
)
from picard.coverart.providers.caa import CoverArtProviderCaa as CoverArtProviderCaa

class CaaCoverArtImageRg(CaaCoverArtImage): ...
class CaaThumbnailCoverArtImageRg(CaaThumbnailCoverArtImage): ...

class CoverArtProviderCaaReleaseGroup(CoverArtProviderCaa):
    NAME: str
    TITLE: Incomplete
    OPTIONS: Incomplete
    ignore_json_not_found_error: bool
    coverartimage_class = CaaCoverArtImageRg
    coverartimage_thumbnail_class = CaaThumbnailCoverArtImageRg
    def enabled(self): ...
