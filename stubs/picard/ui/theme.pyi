from PyQt5 import QtWidgets
from _typeshed import Incomplete
from enum import Enum
from picard import log as log
from picard.config import get_config as get_config
from picard.const.sys import (
    IS_HAIKU as IS_HAIKU,
    IS_MACOS as IS_MACOS,
    IS_WIN as IS_WIN,
)
from typing import NamedTuple, Optional

OS_SUPPORTS_THEMES: bool

class UiTheme(Enum):
    DEFAULT = "default"
    DARK = "dark"
    LIGHT = "light"
    SYSTEM = "system"

AVAILABLE_UI_THEMES: Incomplete

class SyntaxTheme(NamedTuple):
    func: Incomplete
    var: Incomplete
    escape: Incomplete
    special: Incomplete
    noop: Incomplete

light_syntax_theme: Incomplete
dark_syntax_theme: Incomplete

class MacOverrideStyle(QtWidgets.QProxyStyle):
    def styleHint(
        self,
        hint: QtWidgets.QStyle.StyleHint,
        option: Optional[QtWidgets.QStyleOption] = ...,
        widget: Optional[QtWidgets.QWidget] = ...,
        returnData: Optional[QtWidgets.QStyleHintReturn] = ...,
    ) -> int: ...

class BaseTheme:
    def __init__(self) -> None: ...
    def setup(self, app) -> None: ...
    @property
    def is_dark_theme(self): ...
    @property
    def accent_color(self) -> None: ...
    @property
    def syntax_theme(self): ...
    def update_palette(self, palette, dark_theme, accent_color) -> None: ...

class WindowsTheme(BaseTheme):
    def setup(self, app) -> None: ...
    @property
    def is_dark_theme(self): ...
    @property
    def accent_color(self): ...
    def update_palette(self, palette, dark_theme, accent_color) -> None: ...

theme: Incomplete
dark_appearance: bool
appearance: Incomplete
basic_appearance: Incomplete

class MacTheme(BaseTheme):
    def setup(self, app) -> None: ...
    @property
    def is_dark_theme(self): ...
    def update_palette(self, palette, dark_theme, accent_color) -> None: ...

def setup(app) -> None: ...
