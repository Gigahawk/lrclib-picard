from PyQt5 import QtGui, QtWidgets
from _typeshed import Incomplete
from picard import log as log
from picard.config import IntOption as IntOption, get_config as get_config
from picard.ui import (
    FONT_FAMILY_MONOSPACE as FONT_FAMILY_MONOSPACE,
    PicardDialog as PicardDialog,
)
from picard.ui.colors import interface_colors as interface_colors
from picard.util import (
    reconnect as reconnect,
    wildcards_to_regex_pattern as wildcards_to_regex_pattern,
)

class LogViewDialog(PicardDialog):
    defaultsize: Incomplete
    doc: Incomplete
    textCursor: Incomplete
    browser: Incomplete
    vbox: Incomplete
    def __init__(self, title, parent: Incomplete | None = None) -> None: ...

class LogViewCommon(LogViewDialog):
    displaying: bool
    log_tail: Incomplete
    def __init__(self, log_tail, *args, **kwargs) -> None: ...
    def closeEvent(self, event) -> None: ...
    def hideEvent(self, event) -> None: ...
    def showEvent(self, event) -> None: ...
    prev: Incomplete
    def display(self, clear: bool = False) -> None: ...
    def clear(self) -> None: ...

class Highlighter(QtGui.QSyntaxHighlighter):
    fmt: Incomplete
    reg: Incomplete
    def __init__(self, string, parent: Incomplete | None = None) -> None: ...
    def highlightBlock(self, text) -> None: ...

class VerbosityMenu(QtWidgets.QMenu):
    verbosity_changed: Incomplete
    action_group: Incomplete
    actions: Incomplete
    def __init__(self, parent: Incomplete | None = None) -> None: ...
    def set_verbosity(self, level) -> None: ...

class LogView(LogViewCommon):
    options: Incomplete
    verbosity: Incomplete
    hl_text: str
    hl: Incomplete
    hbox: Incomplete
    verbosity_menu_button: Incomplete
    verbosity_menu: Incomplete
    highlight_text: Incomplete
    highlight_button: Incomplete
    clear_highlight_button: Incomplete
    clear_log_button: Incomplete
    save_log_as_button: Incomplete
    def __init__(self, parent: Incomplete | None = None) -> None: ...
    def show(self) -> None: ...
    def display(self, clear: bool = False) -> None: ...
    def is_shown(self, logitem): ...

class HistoryView(LogViewCommon):
    def __init__(self, parent: Incomplete | None = None) -> None: ...
