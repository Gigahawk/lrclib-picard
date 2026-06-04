from _typeshed import Incomplete
from picard.config import ListOption as ListOption, get_config as get_config
from picard.ui.options import (
    OptionsPage as OptionsPage,
    register_options_page as register_options_page,
)
from picard.ui.ui_options_interface_top_tags import (
    Ui_InterfaceTopTagsOptionsPage as Ui_InterfaceTopTagsOptionsPage,
)

class InterfaceTopTagsOptionsPage(OptionsPage):
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
    def restore_defaults(self) -> None: ...
