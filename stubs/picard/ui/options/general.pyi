from _typeshed import Incomplete
from picard.config import (
    BoolOption as BoolOption,
    IntOption as IntOption,
    TextOption as TextOption,
    get_config as get_config,
)
from picard.const import (
    DEFAULT_PROGRAM_UPDATE_LEVEL as DEFAULT_PROGRAM_UPDATE_LEVEL,
    MUSICBRAINZ_SERVERS as MUSICBRAINZ_SERVERS,
    PROGRAM_UPDATE_LEVELS as PROGRAM_UPDATE_LEVELS,
)
from picard.ui.options import (
    OptionsPage as OptionsPage,
    register_options_page as register_options_page,
)
from picard.ui.ui_options_general import Ui_GeneralOptionsPage as Ui_GeneralOptionsPage
from picard.util.mbserver import is_official_server as is_official_server

class GeneralOptionsPage(OptionsPage):
    NAME: str
    TITLE: Incomplete
    PARENT: Incomplete
    SORT_ORDER: int
    ACTIVE: bool
    HELP_URL: str
    options: Incomplete
    ui: Incomplete
    def __init__(self, parent: Incomplete | None = None) -> None: ...
    def load(self) -> None: ...
    def set_update_level(self, value) -> None: ...
    def save(self) -> None: ...
    def update_server_host(self) -> None: ...
    def update_login_logout(self, error_msg: Incomplete | None = None) -> None: ...
    def login(self) -> None: ...
    def on_login_finished(
        self, successful, error_msg: Incomplete | None = None
    ) -> None: ...
    def logout(self) -> None: ...
    def on_logout_finished(
        self, successful, error_msg: Incomplete | None = None
    ) -> None: ...
    def restore_defaults(self) -> None: ...
