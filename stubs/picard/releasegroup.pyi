from _typeshed import Incomplete
from picard import log as log
from picard.dataobj import DataObject as DataObject
from picard.mbjson import (
    countries_from_node as countries_from_node,
    label_info_from_node as label_info_from_node,
    media_formats_from_node as media_formats_from_node,
)
from picard.metadata import Metadata as Metadata
from picard.util import countries_shortlist as countries_shortlist, uniqify as uniqify

class ReleaseGroup(DataObject):
    metadata: Incomplete
    loaded: bool
    versions: Incomplete
    version_headings: str
    loaded_albums: Incomplete
    refcount: int
    def __init__(self, rg_id) -> None: ...
    def load_versions(self, callback) -> None: ...
    def remove_album(self, album_id) -> None: ...
