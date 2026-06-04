from _typeshed import Incomplete
from picard.config import TextOption as TextOption, get_config as get_config
from picard.ui.options import (
    OptionsPage as OptionsPage,
    register_options_page as register_options_page,
)
from picard.ui.ui_options_cdlookup import (
    Ui_CDLookupOptionsPage as Ui_CDLookupOptionsPage,
)
from picard.util.cdrom import (
    AUTO_DETECT_DRIVES as AUTO_DETECT_DRIVES,
    DEFAULT_DRIVES as DEFAULT_DRIVES,
    get_cdrom_drives as get_cdrom_drives,
)

class CDLookupOptionsPage(OptionsPage):
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
