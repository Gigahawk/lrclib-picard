from PyQt5 import QtWidgets
from _typeshed import Incomplete
from collections.abc import Generator
from picard.ui import PicardDialog as PicardDialog
from picard.ui.util import (
    StandardButton as StandardButton,
    qlistwidget_items as qlistwidget_items,
)

class ArrowButton(QtWidgets.QPushButton):
    def __init__(
        self,
        icon_name,
        command: Incomplete | None = None,
        parent: Incomplete | None = None,
    ) -> None: ...

class ArrowsColumn(QtWidgets.QWidget):
    selection_list: Incomplete
    ignore_list: Incomplete
    callback: Incomplete
    button_add: Incomplete
    button_add_all: Incomplete
    button_remove: Incomplete
    button_remove_all: Incomplete
    def __init__(
        self,
        selection_list,
        ignore_list,
        callback: Incomplete | None = None,
        reverse: bool = False,
        parent: Incomplete | None = None,
    ) -> None: ...
    def move_from_ignore(self) -> None: ...
    def move_all_from_ignore(self) -> None: ...
    def move_to_ignore(self) -> None: ...
    def move_all_to_ignore(self) -> None: ...

class ListBox(QtWidgets.QListWidget):
    LISTBOX_WIDTH: int
    LISTBOX_HEIGHT: int
    def __init__(self, parent: Incomplete | None = None) -> None: ...
    def move_item(self, item, target_list) -> None: ...
    def move_selected_items(
        self, target_list, callback: Incomplete | None = None
    ) -> None: ...
    def move_all_items(
        self, target_list, callback: Incomplete | None = None
    ) -> None: ...
    def all_items_data(self, role=...) -> Generator[Incomplete]: ...

class CAATypesSelectorDialog(PicardDialog):
    help_url: str
    layout: Incomplete
    list_include: Incomplete
    list_exclude: Incomplete
    list_ignore: Incomplete
    arrows_include: Incomplete
    arrows_exclude: Incomplete
    buttonbox: Incomplete
    def __init__(
        self,
        parent: Incomplete | None = None,
        types_include: Incomplete | None = None,
        types_exclude: Incomplete | None = None,
        default_include: Incomplete | None = None,
        default_exclude: Incomplete | None = None,
        known_types: Incomplete | None = None,
    ) -> None: ...
    def move_all_to_include_list(self) -> None: ...
    def move_all_to_exclude_list(self) -> None: ...
    def move_all_to_ignore_list(self) -> None: ...
    def fill_lists(self, includes, excludes) -> None: ...
    @property
    def included(self): ...
    @property
    def excluded(self): ...
    def clear_focus(self, lists) -> None: ...
    def reset_to_defaults(self) -> None: ...
    def set_buttons_enabled_state(self) -> None: ...

def display_caa_types_selector(**kwargs): ...
