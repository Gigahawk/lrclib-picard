from _typeshed import Incomplete
from mutagen._file import FileType
from mutagen._util import MutagenError
from mutagen.ac3 import AC3

native_ac3: bool

class AC3Error(MutagenError): ...

class AC3Info:
    def __init__(self, fileobj) -> None: ...
    @staticmethod
    def pprint(): ...

class AC3(FileType):
    info: Incomplete
    def load(self, filething, *args, **kwargs) -> None: ...
    @staticmethod
    def score(filename, fileobj, header): ...

class AC3APEv2(AC3):
    tags: Incomplete
    def load(self, filething) -> None: ...
    def add_tags(self) -> None: ...
