from _typeshed import Incomplete

UPDATE_LINES_TO_SHOW: int

class PluginUpdatesDialog:
    show_again: bool
    msg: Incomplete
    cb: Incomplete
    def __init__(self, parent, plugin_names) -> None: ...
    def show(self): ...
