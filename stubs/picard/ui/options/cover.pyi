from _typeshed import Incomplete
from picard.config import (
    BoolOption as BoolOption,
    ListOption as ListOption,
    Option as Option,
    TextOption as TextOption,
    get_config as get_config,
)
from picard.const import DEFAULT_COVER_IMAGE_FILENAME as DEFAULT_COVER_IMAGE_FILENAME
from picard.coverart.providers import cover_art_providers as cover_art_providers
from picard.ui.checkbox_list_item import CheckboxListItem as CheckboxListItem
from picard.ui.moveable_list_view import MoveableListView as MoveableListView
from picard.ui.options import (
    OptionsPage as OptionsPage,
    register_options_page as register_options_page,
)
from picard.ui.ui_options_cover import Ui_CoverOptionsPage as Ui_CoverOptionsPage
from picard.ui.util import qlistwidget_items as qlistwidget_items

class CoverOptionsPage(OptionsPage):
    NAME: str
    TITLE: Incomplete
    PARENT: Incomplete
    SORT_ORDER: int
    ACTIVE: bool
    HELP_URL: str
    options: Incomplete
    ui: Incomplete
    move_view: Incomplete
    def __init__(self, parent: Incomplete | None = None) -> None: ...
    def restore_defaults(self) -> None: ...
    def load(self) -> None: ...
    def save(self) -> None: ...
    def update_ca_providers_groupbox_state(self) -> None: ...
