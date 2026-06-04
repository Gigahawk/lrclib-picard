from _typeshed import Incomplete
from picard.config import get_config as get_config

class SaveWarningDialog:
    disable: bool
    msg: Incomplete
    cb: Incomplete
    def __init__(self, parent, file_count) -> None: ...
    def show(self): ...
