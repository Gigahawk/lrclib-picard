from PyQt5 import QtWidgets
from _typeshed import Incomplete

class TristateSortHeaderView(QtWidgets.QHeaderView):
    STATE_NONE: int
    STATE_SECTION_MOVED_OR_RESIZED: int
    def __init__(self, orientation, parent: Incomplete | None = None) -> None: ...
    def mouseReleaseEvent(self, event) -> None: ...
    is_locked: Incomplete
    def lock(self, is_locked) -> None: ...
