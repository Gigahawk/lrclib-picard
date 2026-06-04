from PyQt5 import QtGui
from _typeshed import Incomplete
from picard.config import (
    BoolOption as BoolOption,
    Option as Option,
    TextOption as TextOption,
    get_config as get_config,
)
from picard.const.sys import IS_WIN as IS_WIN
from picard.ui import PicardDialog as PicardDialog
from picard.ui.options import (
    OptionsCheckError as OptionsCheckError,
    OptionsPage as OptionsPage,
    register_options_page as register_options_page,
)
from picard.ui.ui_options_renaming_compat import (
    Ui_RenamingCompatOptionsPage as Ui_RenamingCompatOptionsPage,
)
from picard.ui.ui_win_compat_dialog import Ui_WinCompatDialog as Ui_WinCompatDialog
from picard.util import system_supports_long_paths as system_supports_long_paths

DEFAULT_REPLACEMENT: str

class RenamingCompatOptionsPage(OptionsPage):
    NAME: str
    TITLE: Incomplete
    PARENT: str
    ACTIVE: bool
    HELP_URL: str
    options: Incomplete
    options_changed: Incomplete
    win_compat_replacements: Incomplete
    ui: Incomplete
    def __init__(self, parent: Incomplete | None = None) -> None: ...
    def load(self) -> None: ...
    def save(self) -> None: ...
    def check(self) -> None: ...
    def toggle_windows_long_paths(self, state) -> None: ...
    def on_options_changed(self) -> None: ...
    def get_options(self): ...
    def open_win_compat_dialog(self) -> None: ...

class NoDirectorySeparatorValidator(QtGui.QValidator):
    def validate(self, text: str, pos): ...

class WinCompatReplacementValidator(QtGui.QValidator):
    def validate(self, text: str, pos): ...

class WinCompatDialog(PicardDialog):
    replacements: Incomplete
    ui: Incomplete
    def __init__(self, replacements, parent: Incomplete | None = None) -> None: ...
    def load(self) -> None: ...
    def accept(self) -> None: ...
    def restore_defaults(self) -> None: ...
