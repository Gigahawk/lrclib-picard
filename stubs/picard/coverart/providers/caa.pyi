from _typeshed import Incomplete
from picard import log as log
from picard.config import (
    BoolOption as BoolOption,
    IntOption as IntOption,
    ListOption as ListOption,
    get_config as get_config,
)
from picard.const import CAA_URL as CAA_URL
from picard.coverart.image import (
    CaaCoverArtImage as CaaCoverArtImage,
    CaaThumbnailCoverArtImage as CaaThumbnailCoverArtImage,
)
from picard.coverart.providers.provider import (
    CoverArtProvider as CoverArtProvider,
    ProviderOptions as ProviderOptions,
)
from picard.coverart.utils import (
    CAA_TYPES as CAA_TYPES,
    translate_caa_type as translate_caa_type,
)
from picard.ui.caa_types_selector import (
    display_caa_types_selector as display_caa_types_selector,
)
from picard.ui.ui_provider_options_caa import Ui_CaaOptions as Ui_CaaOptions
from picard.webservice import ratecontrol as ratecontrol
from typing import NamedTuple

class CaaSizeItem(NamedTuple):
    thumbnail: Incomplete
    label: Incomplete

def caa_url_fallback_list(desired_size, thumbnails): ...

class ProviderOptionsCaa(ProviderOptions):
    TITLE: Incomplete
    HELP_URL: str
    options: Incomplete
    def __init__(self, parent: Incomplete | None = None) -> None: ...
    caa_image_types: Incomplete
    caa_image_types_to_omit: Incomplete
    def restore_defaults(self) -> None: ...
    def load(self) -> None: ...
    def save(self) -> None: ...
    def update_caa_types(self) -> None: ...
    def select_caa_types(self) -> None: ...

class CoverArtProviderCaa(CoverArtProvider):
    NAME: str
    TITLE: Incomplete
    OPTIONS = ProviderOptionsCaa
    ignore_json_not_found_error: bool
    coverartimage_class = CaaCoverArtImage
    coverartimage_thumbnail_class = CaaThumbnailCoverArtImage
    restrict_types: Incomplete
    included_types: Incomplete
    excluded_types: Incomplete
    included_types_count: Incomplete
    def __init__(self, coverart) -> None: ...
    def enabled(self): ...
    def queue_images(self): ...
