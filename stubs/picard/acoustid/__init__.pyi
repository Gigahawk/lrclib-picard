from PyQt5 import QtCore
from _typeshed import Incomplete
from enum import IntEnum
from picard import log as log
from picard.acoustid.recordings import RecordingResolver as RecordingResolver
from picard.config import get_config as get_config
from picard.const import (
    DEFAULT_FPCALC_THREADS as DEFAULT_FPCALC_THREADS,
    FPCALC_NAMES as FPCALC_NAMES,
)
from picard.const.sys import IS_WIN as IS_WIN
from picard.file import File as File
from picard.util import (
    find_executable as find_executable,
    win_prefix_longpath as win_prefix_longpath,
)
from picard.webservice.api_helpers import AcoustIdAPIHelper as AcoustIdAPIHelper
from typing import NamedTuple

class FpcalcExit(IntEnum):
    NOERROR = 0
    DECODING_ERROR = 3

def get_score(node): ...
def get_fpcalc(config: Incomplete | None = None): ...
def find_fpcalc(): ...

class AcoustIDTask(NamedTuple):
    file: Incomplete
    next_func: Incomplete

class AcoustIDClient(QtCore.QObject):
    def __init__(self, acoustid_api: AcoustIdAPIHelper) -> None: ...
    def init(self) -> None: ...
    def done(self) -> None: ...
    def get_max_processes(self): ...
    def analyze(self, file, next_func) -> None: ...
    def fingerprint(self, file, next_func) -> None: ...
    def stop_analyze(self, file) -> None: ...
