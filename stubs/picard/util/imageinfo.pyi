from _typeshed import Incomplete
from collections.abc import Generator
from picard.util.bitreader import LSBBitReader as LSBBitReader

class IdentificationError(Exception): ...
class NotEnoughData(IdentificationError): ...
class UnrecognizedFormat(IdentificationError): ...
class UnexpectedError(IdentificationError): ...

class IdentifyImageType:
    mime: str
    extension: str
    w: int
    h: int
    data: Incomplete
    datalen: Incomplete
    def __init__(self, data) -> None: ...
    def read(self): ...
    def match(self) -> None: ...
    @classmethod
    def all_extensions(cls): ...

class IdentifyJPEG(IdentifyImageType):
    mime: str
    extension: str
    def match(self): ...
    @classmethod
    def all_extensions(cls): ...

class IdentifyGIF(IdentifyImageType):
    mime: str
    extension: str
    def match(self): ...

class IdentifyPDF(IdentifyImageType):
    mime: str
    extension: str
    def match(self): ...

class IdentifyPNG(IdentifyImageType):
    mime: str
    extension: str
    def match(self): ...

class IdentifyWebP(IdentifyImageType):
    mime: str
    extension: str
    def match(self): ...

TIFF_BYTE_ORDER_LSB: bytes
TIFF_BYTE_ORDER_MSB: bytes
TIFF_TAG_IMAGE_LENGTH: int
TIFF_TAG_IMAGE_WIDTH: int
TIFF_TYPE_SHORT: int
TIFF_TYPE_LONG: int

class IdentifyTiff(IdentifyImageType):
    mime: str
    extension: str
    def match(self): ...
    @classmethod
    def all_extensions(cls): ...

knownimagetypes: Incomplete

def identify(data): ...
def supports_mime_type(mime): ...
def get_supported_extensions() -> Generator[Incomplete, Incomplete]: ...
