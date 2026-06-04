from _typeshed import Incomplete
from collections.abc import Generator
from picard import log as log
from picard.config import (
    Option as Option,
    get_config as get_config,
    load_new_config as load_new_config,
)
from picard.config_upgrade import upgrade_config as upgrade_config
from picard.ui.options import (
    OptionsPage as OptionsPage,
    register_options_page as register_options_page,
)
from picard.ui.ui_options_maintenance import (
    Ui_MaintenanceOptionsPage as Ui_MaintenanceOptionsPage,
)
from picard.util import open_local_path as open_local_path

OPTIONS_NOT_IN_PAGES: Incomplete

class MaintenanceOptionsPage(OptionsPage):
    NAME: str
    TITLE: Incomplete
    PARENT: str
    SORT_ORDER: int
    ACTIVE: bool
    HELP_URL: str
    options: Incomplete
    signal_reload: Incomplete
    ui: Incomplete
    def __init__(self, parent: Incomplete | None = None) -> None: ...
    def load(self) -> None: ...
    def open_config_dir(self) -> None: ...
    def save_backup(self) -> None: ...
    def load_backup(self) -> None: ...
    def column_items(self, column) -> Generator[Incomplete]: ...
    def selected_options(self) -> Generator[Incomplete]: ...
    def select_all_changed(self) -> None: ...
    def save(self) -> None: ...
    def make_setting_value_text(self, key): ...
    def enable_cleanup_changed(self) -> None: ...
