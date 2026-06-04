from PyQt5 import QtWidgets
from _typeshed import Incomplete
from picard.config import get_config as get_config
from picard.ui.tablebaseddialog import TableBasedDialog as TableBasedDialog
from picard.ui.util import StandardButton as StandardButton
from picard.util import icontheme as icontheme, restore_method as restore_method
from typing import NamedTuple

class SearchBox(QtWidgets.QWidget):
    search_action: Incomplete
    force_advanced_search: bool
    use_advanced_search: Incomplete
    def __init__(
        self, parent, force_advanced_search: Incomplete | None = None
    ) -> None: ...
    def focus_in_event(self, event) -> None: ...
    layout: Incomplete
    search_row_widget: Incomplete
    search_row_layout: Incomplete
    search_edit: Incomplete
    search_button: Incomplete
    adv_opt_row_widget: Incomplete
    adv_opt_row_layout: Incomplete
    use_adv_search_syntax: Incomplete
    adv_syntax_help: Incomplete
    def setupUi(self) -> None: ...
    def search(self) -> None: ...
    def restore_checkbox_state(self) -> None: ...
    def update_advanced_syntax_setting(self) -> None: ...
    def enable_search(self) -> None: ...
    def trigger_search_action(self) -> None: ...
    def get_query(self): ...
    def set_query(self, query): ...
    query: Incomplete

class Retry(NamedTuple):
    function: Incomplete
    query: Incomplete

class SearchDialog(TableBasedDialog):
    accept_button_title: str
    search_results: Incomplete
    show_search: Incomplete
    search_type: Incomplete
    force_advanced_search: Incomplete
    search_box: Incomplete
    def __init__(
        self,
        parent,
        accept_button_title,
        show_search: bool = True,
        search_type: Incomplete | None = None,
        force_advanced_search: Incomplete | None = None,
    ) -> None: ...
    @property
    def use_advanced_search(self): ...
    def get_value_for_row_id(self, row, value): ...
    verticalLayout: Incomplete
    center_widget: Incomplete
    center_layout: Incomplete
    buttonBox: Incomplete
    search_browser_button: Incomplete
    accept_button: Incomplete
    def setupUi(self) -> None: ...
    def show_progress(self) -> None: ...
    def show_error(self, error, show_retry_button: bool = False) -> None: ...
    def network_error(self, reply, error) -> None: ...
    def no_results_found(self) -> None: ...
    def search_browser(self) -> None: ...
    def restore_state(self) -> None: ...
    def search_box_text(self, text) -> None: ...
