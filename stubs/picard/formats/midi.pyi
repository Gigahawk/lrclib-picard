from _typeshed import Incomplete
from picard import log as log
from picard.file import File as File
from picard.metadata import Metadata as Metadata
from picard.util import encode_filename as encode_filename

class MIDIFile(File):
    EXTENSIONS: Incomplete
    NAME: str
    @classmethod
    def supports_tag(cls, name): ...
    def can_analyze(self): ...
