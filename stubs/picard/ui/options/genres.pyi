from _typeshed import Incomplete
from picard.config import (
    BoolOption as BoolOption,
    IntOption as IntOption,
    TextOption as TextOption,
    get_config as get_config,
)
from picard.track import TagGenreFilter as TagGenreFilter
from picard.ui.options import (
    OptionsPage as OptionsPage,
    register_options_page as register_options_page,
)
from picard.ui.ui_options_genres import Ui_GenresOptionsPage as Ui_GenresOptionsPage

TOOLTIP_GENRES_FILTER: Incomplete
TOOLTIP_TEST_GENRES_FILTER: Incomplete

class GenresOptionsPage(OptionsPage):
    NAME: str
    TITLE: Incomplete
    PARENT: str
    SORT_ORDER: int
    ACTIVE: bool
    HELP_URL: str
    options: Incomplete
    ui: Incomplete
    fmt_keep: Incomplete
    fmt_skip: Incomplete
    fmt_clear: Incomplete
    def __init__(self, parent: Incomplete | None = None) -> None: ...
    def load(self) -> None: ...
    def save(self) -> None: ...
    def update_test_genres_filter(self) -> None: ...
