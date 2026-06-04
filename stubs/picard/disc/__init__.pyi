from PyQt5 import QtCore
from _typeshed import Incomplete
from picard import log as log
from picard.ui.cdlookup import CDLookupDialog as CDLookupDialog
from picard.util.mbserver import build_submission_url as build_submission_url

class Disc(QtCore.QObject):
    id: Incomplete
    mcn: Incomplete
    tracks: int
    toc_string: Incomplete
    def __init__(self, id: Incomplete | None = None) -> None: ...
    def read(self, device: Incomplete | None = None) -> None: ...
    def put(self, toc) -> None: ...
    @property
    def submission_url(self): ...
    def lookup(self) -> None: ...

discid_version: Incomplete
