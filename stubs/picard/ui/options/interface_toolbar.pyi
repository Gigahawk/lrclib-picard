from PyQt5 import QtWidgets
from _typeshed import Incomplete
from picard.config import ListOption as ListOption, get_config as get_config
from picard.ui import PicardDialog as PicardDialog
from picard.ui.moveable_list_view import MoveableListView as MoveableListView
from picard.ui.options import (
    OptionsPage as OptionsPage,
    register_options_page as register_options_page,
)
from picard.ui.ui_options_interface_toolbar import (
    Ui_InterfaceToolbarOptionsPage as Ui_InterfaceToolbarOptionsPage,
)
from picard.ui.util import qlistwidget_items as qlistwidget_items
from picard.util import icontheme as icontheme

class InterfaceToolbarOptionsPage(OptionsPage):
    NAME: str
    TITLE: Incomplete
    PARENT: str
    SORT_ORDER: int
    ACTIVE: bool
    HELP_URL: str
    SEPARATOR: Incomplete
    TOOLBAR_BUTTONS: Incomplete
    ACTION_NAMES: Incomplete
    options: Incomplete
    ui: Incomplete
    move_view: Incomplete
    update_buttons: Incomplete
    def __init__(self, parent: Incomplete | None = None) -> None: ...
    def load(self) -> None: ...
    def save(self) -> None: ...
    def restore_defaults(self) -> None: ...
    def starting_directory_browse(self) -> None: ...
    def populate_action_list(self) -> None: ...
    def update_action_buttons(self) -> None: ...
    def add_to_toolbar(self) -> None: ...
    def insert_separator(self) -> None: ...
    def remove_action(self) -> None: ...
    def update_layout_config(self) -> None: ...

class ToolbarListItem(QtWidgets.QListWidgetItem):
    action_name: Incomplete
    def __init__(self, action_name, *args, **kwargs) -> None: ...

class AddActionDialog(PicardDialog):
    action_list: Incomplete
    combo_box: Incomplete
    def __init__(self, action_list, *args, **kwargs) -> None: ...
    def selected_action(self): ...
    @staticmethod
    def get_selected_action(action_list, parent: Incomplete | None = None): ...
