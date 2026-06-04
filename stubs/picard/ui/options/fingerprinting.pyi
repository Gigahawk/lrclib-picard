from PyQt5 import QtGui
from _typeshed import Incomplete
from picard.acoustid import find_fpcalc as find_fpcalc
from picard.config import (
    BoolOption as BoolOption,
    IntOption as IntOption,
    TextOption as TextOption,
    get_config as get_config,
)
from picard.const import DEFAULT_FPCALC_THREADS as DEFAULT_FPCALC_THREADS
from picard.ui.options import (
    OptionsCheckError as OptionsCheckError,
    OptionsPage as OptionsPage,
    register_options_page as register_options_page,
)
from picard.ui.ui_options_fingerprinting import (
    Ui_FingerprintingOptionsPage as Ui_FingerprintingOptionsPage,
)
from picard.util import webbrowser2 as webbrowser2

class ApiKeyValidator(QtGui.QValidator):
    def validate(self, input, pos): ...

class FingerprintingOptionsPage(OptionsPage):
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
    def update_groupboxes(self) -> None: ...
    def acoustid_fpcalc_browse(self) -> None: ...
    def acoustid_fpcalc_download(self) -> None: ...
    def acoustid_apikey_get(self) -> None: ...
    def check(self) -> None: ...
    def display_error(self, error) -> None: ...
