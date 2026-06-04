from _typeshed import Incomplete
from collections.abc import Generator
from picard import i18n as i18n
from typing import NamedTuple

class SettingDesc(NamedTuple):
    name: Incomplete
    title: Incomplete
    fields: Incomplete

class UserProfileGroups:
    SETTINGS_GROUPS: Incomplete
    ALL_SETTINGS: Incomplete
    @classmethod
    def get_setting_groups_list(cls) -> Generator[Incomplete, Incomplete]: ...
