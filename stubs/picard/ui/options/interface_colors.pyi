from PyQt5 import QtWidgets
from _typeshed import Incomplete
from picard.config import Option as Option
from picard.const.sys import IS_MACOS as IS_MACOS
from picard.ui.colors import (
    InterfaceColors as InterfaceColors,
    interface_colors as interface_colors,
)
from picard.ui.options import (
    OptionsPage as OptionsPage,
    register_options_page as register_options_page,
)
from picard.ui.ui_options_interface_colors import (
    Ui_InterfaceColorsOptionsPage as Ui_InterfaceColorsOptionsPage,
)

class ColorButton(QtWidgets.QPushButton):
    color_changed: Incomplete
    color: Incomplete
    def __init__(
        self, initial_color: Incomplete | None = None, parent: Incomplete | None = None
    ) -> None: ...
    def update_color(self) -> None: ...
    def open_color_dialog(self) -> None: ...

def delete_items_of_layout(layout) -> None: ...

class InterfaceColorsOptionsPage(OptionsPage):
    NAME: str
    TITLE: Incomplete
    PARENT: str
    SORT_ORDER: int
    ACTIVE: bool
    HELP_URL: str
    options: Incomplete
    ui: Incomplete
    new_colors: Incomplete
    colors_list: Incomplete
    def __init__(self, parent: Incomplete | None = None) -> None: ...
    def update_color_selectors(self) -> None: ...
    def load(self) -> None: ...
    def save(self) -> None: ...
    def restore_defaults(self) -> None: ...
