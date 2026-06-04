from _typeshed import Incomplete
from picard.config import (
    BoolOption as BoolOption,
    TextOption as TextOption,
    get_config as get_config,
)
from picard.formats.wav import WAVFile as WAVFile
from picard.ui.options import (
    OptionsPage as OptionsPage,
    register_options_page as register_options_page,
)
from picard.ui.ui_options_tags_compatibility_wave import (
    Ui_TagsCompatibilityOptionsPage as Ui_TagsCompatibilityOptionsPage,
)

class TagsCompatibilityWaveOptionsPage(OptionsPage):
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
