from mutagen import StreamInfo
from mutagen.apev2 import APEv2File, delete as delete, error
from mutagen.tak import Open as Open, TAK as TAK

__all__ = ["TAK", "Open", "delete"]

class TAKHeaderError(error): ...

class TAKInfo(StreamInfo):
    def __init__(self, fileobj) -> None: ...
    @staticmethod
    def pprint(): ...

class TAK(APEv2File):
    @staticmethod
    def score(filename, fileobj, header): ...

Open = TAK
