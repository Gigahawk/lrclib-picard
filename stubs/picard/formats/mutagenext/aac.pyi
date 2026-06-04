from _typeshed import Incomplete
from mutagen.aac import AAC

class AACAPEv2(AAC):
    tags: Incomplete
    def load(self, filething) -> None: ...
    def add_tags(self) -> None: ...
