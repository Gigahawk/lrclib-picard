from _typeshed import Incomplete
from collections.abc import Generator
from picard.config import TextOption as TextOption, get_config as get_config
from picard.coverart.image import LocalFileCoverArtImage as LocalFileCoverArtImage
from picard.coverart.providers.provider import (
    CoverArtProvider as CoverArtProvider,
    ProviderOptions as ProviderOptions,
)
from picard.coverart.utils import CAA_TYPES as CAA_TYPES
from picard.ui.ui_provider_options_local import Ui_LocalOptions as Ui_LocalOptions

class ProviderOptionsLocal(ProviderOptions):
    HELP_URL: str
    options: Incomplete
    def __init__(self, parent: Incomplete | None = None) -> None: ...
    def set_local_cover_regex_default(self) -> None: ...
    def load(self) -> None: ...
    def save(self) -> None: ...

class CoverArtProviderLocal(CoverArtProvider):
    NAME: str
    TITLE: Incomplete
    OPTIONS = ProviderOptionsLocal
    def queue_images(self): ...
    def get_types(self, string): ...
    def find_local_images(self, current_dir, match_re) -> Generator[Incomplete]: ...
