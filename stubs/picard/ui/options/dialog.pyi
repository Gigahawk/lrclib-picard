from _typeshed import Incomplete
from picard import log as log
from picard.config import (
    ListOption as ListOption,
    SettingConfigSection as SettingConfigSection,
    TextOption as TextOption,
    get_config as get_config,
)
from picard.profile import UserProfileGroups as UserProfileGroups
from picard.ui import (
    HashableTreeWidgetItem as HashableTreeWidgetItem,
    PicardDialog as PicardDialog,
    SingletonDialog as SingletonDialog,
)
from picard.ui.options import (
    OptionsCheckError as OptionsCheckError,
    advanced as advanced,
    cdlookup as cdlookup,
    cover as cover,
    fingerprinting as fingerprinting,
    general as general,
    genres as genres,
    interface as interface,
    interface_colors as interface_colors,
    interface_toolbar as interface_toolbar,
    interface_top_tags as interface_top_tags,
    maintenance as maintenance,
    matching as matching,
    metadata as metadata,
    network as network,
    plugins as plugins,
    profiles as profiles,
    ratings as ratings,
    releases as releases,
    renaming as renaming,
    renaming_compat as renaming_compat,
    scripting as scripting,
    tags as tags,
    tags_compatibility_aac as tags_compatibility_aac,
    tags_compatibility_ac3 as tags_compatibility_ac3,
    tags_compatibility_id3 as tags_compatibility_id3,
    tags_compatibility_wave as tags_compatibility_wave,
)
from picard.ui.theme import theme as theme
from picard.ui.ui_options_attached_profiles import (
    Ui_AttachedProfilesDialog as Ui_AttachedProfilesDialog,
)
from picard.ui.util import StandardButton as StandardButton
from picard.util import restore_method as restore_method

class OptionsDialog(PicardDialog, SingletonDialog):
    options: Incomplete
    suspend_signals: bool
    default_item: Incomplete
    def add_pages(self, parent, default_page, parent_item) -> None: ...
    ui: Incomplete
    pages: Incomplete
    item_to_page: Incomplete
    page_to_item: Incomplete
    profile_page: Incomplete
    maintenance_page: Incomplete
    first_enter: bool
    def __init__(
        self, default_page: Incomplete | None = None, parent: Incomplete | None = None
    ) -> None: ...
    def load_all_pages(self) -> None: ...
    def page_has_profile_options(self, page): ...
    def show_attached_profiles_dialog(self): ...
    def update_from_profile_changes(self) -> None: ...
    def get_working_profile_data(self): ...
    def highlight_enabled_profile_options(
        self, load_settings: bool = False
    ) -> None: ...
    def eventFilter(self, object, event): ...
    def get_page(self, name): ...
    def page_has_attached_profiles(self, page, enabled_profiles_only: bool = False): ...
    def set_profiles_button_and_highlight(self, page) -> None: ...
    def switch_page(self) -> None: ...
    def disable_page(self, name) -> None: ...
    @property
    def help_url(self): ...
    def accept(self) -> None: ...
    def saveWindowState(self) -> None: ...
    def restoreWindowState(self) -> None: ...
    def restore_all_defaults(self) -> None: ...
    def restore_page_defaults(self) -> None: ...
    def confirm_reset(self) -> None: ...
    def confirm_reset_all(self) -> None: ...

class AttachedProfilesDialog(PicardDialog):
    NAME: str
    TITLE: Incomplete
    option_group: Incomplete
    ui: Incomplete
    profiles: Incomplete
    settings: Incomplete
    def __init__(
        self,
        parent: Incomplete | None = None,
        option_group: Incomplete | None = None,
        override_profiles: Incomplete | None = None,
        override_settings: Incomplete | None = None,
    ) -> None: ...
    def populate_table(self) -> None: ...
    def close_window(self) -> None: ...
