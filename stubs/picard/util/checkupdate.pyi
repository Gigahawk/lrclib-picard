from PyQt5 import QtCore
from _typeshed import Incomplete
from picard import (
    PICARD_FANCY_VERSION_STR as PICARD_FANCY_VERSION_STR,
    PICARD_VERSION as PICARD_VERSION,
    log as log,
)
from picard.const import (
    PLUGINS_API as PLUGINS_API,
    PROGRAM_UPDATE_LEVELS as PROGRAM_UPDATE_LEVELS,
)
from picard.util import webbrowser2 as webbrowser2
from picard.version import Version as Version, VersionError as VersionError

class UpdateCheckManager(QtCore.QObject):
    def __init__(self, parent: Incomplete | None = None) -> None: ...
    def check_update(
        self,
        show_always: bool = False,
        update_level: int = 0,
        callback: Incomplete | None = None,
    ) -> None: ...
