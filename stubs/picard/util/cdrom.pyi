from _typeshed import Incomplete
from picard import log as log
from picard.config import get_config as get_config
from picard.const.sys import IS_LINUX as IS_LINUX, IS_WIN as IS_WIN

DISCID_NOT_LOADED_MESSAGE: str
DEFAULT_DRIVES: Incomplete
device: Incomplete
LINUX_CDROM_INFO: str
AUTO_DETECT_DRIVES: bool
DRIVE_TYPE_CDROM: int

def get_cdrom_drives(): ...
