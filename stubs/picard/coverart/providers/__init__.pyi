from _typeshed import Incomplete
from collections.abc import Generator
from picard.config import get_config as get_config
from picard.coverart.providers.caa import CoverArtProviderCaa as CoverArtProviderCaa
from picard.coverart.providers.caa_release_group import (
    CoverArtProviderCaaReleaseGroup as CoverArtProviderCaaReleaseGroup,
)
from picard.coverart.providers.local import (
    CoverArtProviderLocal as CoverArtProviderLocal,
)
from picard.coverart.providers.provider import (
    CoverArtProvider as CoverArtProvider,
    ProviderOptions as ProviderOptions,
)
from picard.coverart.providers.urlrels import (
    CoverArtProviderUrlRelationships as CoverArtProviderUrlRelationships,
)
from picard.plugin import ExtensionPoint as ExtensionPoint
from picard.ui.options import register_options_page as register_options_page
from typing import NamedTuple

def register_cover_art_provider(provider) -> None: ...

class ProviderTuple(NamedTuple):
    name: Incomplete
    title: Incomplete
    enabled: Incomplete
    cls: Incomplete

class PInfoTuple(NamedTuple):
    position: Incomplete
    enabled: Incomplete

def cover_art_providers() -> Generator[Incomplete, None, Incomplete]: ...
