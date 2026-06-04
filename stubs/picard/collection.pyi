from PyQt5 import QtCore
from _typeshed import Incomplete
from picard import log as log
from picard.config import get_config as get_config

user_collections: Incomplete

class Collection(QtCore.QObject):
    COLLECTION_ADD: int
    COLLECTION_REMOVE: int
    id: Incomplete
    name: Incomplete
    pending: Incomplete
    size: Incomplete
    releases: Incomplete
    api_action: Incomplete
    def __init__(self, collection_id, name, size) -> None: ...
    def add_releases(self, ids, callback) -> None: ...
    def remove_releases(self, ids, callback) -> None: ...

def get_user_collection(collection_id, name, size, refresh: bool = False): ...
def load_user_collections(callback: Incomplete | None = None) -> None: ...
def add_release_to_user_collections(release_node) -> None: ...
