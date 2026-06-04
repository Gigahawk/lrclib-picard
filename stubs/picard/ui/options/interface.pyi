from _typeshed import Incomplete
from picard.config import (
    BoolOption as BoolOption,
    TextOption as TextOption,
    get_config as get_config,
)
from picard.const.languages import UI_LANGUAGES as UI_LANGUAGES
from picard.const.sys import IS_MACOS as IS_MACOS
from picard.i18n import sort_key as sort_key
from picard.ui.options import (
    OptionsPage as OptionsPage,
    register_options_page as register_options_page,
)
from picard.ui.theme import (
    AVAILABLE_UI_THEMES as AVAILABLE_UI_THEMES,
    OS_SUPPORTS_THEMES as OS_SUPPORTS_THEMES,
    UiTheme as UiTheme,
)
from picard.ui.ui_options_interface import (
    Ui_InterfaceOptionsPage as Ui_InterfaceOptionsPage,
)

class InterfaceOptionsPage(OptionsPage):
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
    def save(self) -> None: ...
    def starting_directory_browse(self) -> None: ...
