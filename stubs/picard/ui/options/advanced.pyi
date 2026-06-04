from _typeshed import Incomplete
from picard.config import (
    BoolOption as BoolOption,
    IntOption as IntOption,
    ListOption as ListOption,
    TextOption as TextOption,
    get_config as get_config,
)
from picard.const import QUERY_LIMIT as QUERY_LIMIT
from picard.ui.options import (
    OptionsPage as OptionsPage,
    register_options_page as register_options_page,
)
from picard.ui.ui_options_advanced import (
    Ui_AdvancedOptionsPage as Ui_AdvancedOptionsPage,
)

class AdvancedOptionsPage(OptionsPage):
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
    def restore_defaults(self) -> None: ...
