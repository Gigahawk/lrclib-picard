from _typeshed import Incomplete
from picard.config import (
    BoolOption as BoolOption,
    IntOption as IntOption,
    TextOption as TextOption,
    get_config as get_config,
)
from picard.ui.options import (
    OptionsPage as OptionsPage,
    register_options_page as register_options_page,
)
from picard.ui.ui_options_network import Ui_NetworkOptionsPage as Ui_NetworkOptionsPage

class NetworkOptionsPage(OptionsPage):
    NAME: str
    TITLE: Incomplete
    PARENT: str
    SORT_ORDER: int
    ACTIVE: bool
    HELP_URL: str
    options: Incomplete
    ui: Incomplete
    def __init__(self, parent: Incomplete | None = None) -> None: ...
    def load(self) -> None: ...
    def save(self) -> None: ...
