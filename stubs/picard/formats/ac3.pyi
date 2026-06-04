from .mutagenext import ac3 as ac3
from _typeshed import Incomplete
from picard import log as log
from picard.config import get_config as get_config
from picard.formats.apev2 import APEv2File as APEv2File
from picard.util import encode_filename as encode_filename

class AC3File(APEv2File):
    EXTENSIONS: Incomplete
    NAME: str
    @classmethod
    def supports_tag(cls, name): ...
