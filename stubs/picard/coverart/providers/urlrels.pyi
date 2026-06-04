from _typeshed import Incomplete
from picard import log as log
from picard.coverart.image import CoverArtImage as CoverArtImage
from picard.coverart.providers.provider import CoverArtProvider as CoverArtProvider

class CoverArtProviderUrlRelationships(CoverArtProvider):
    NAME: str
    TITLE: Incomplete
    def queue_images(self): ...
