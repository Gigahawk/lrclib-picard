from PyQt5 import QtWidgets
from _typeshed import Incomplete
from picard.album import Album as Album
from picard.browser.filelookup import FileLookup as FileLookup
from picard.cluster import Cluster as Cluster
from picard.config import (
    BoolOption as BoolOption,
    Option as Option,
    get_config as get_config,
)
from picard.file import File as File
from picard.metadata import MULTI_VALUED_JOINER as MULTI_VALUED_JOINER
from picard.track import Track as Track
from picard.ui.colors import interface_colors as interface_colors
from picard.ui.edittagdialog import (
    EditTagDialog as EditTagDialog,
    TagEditorDelegate as TagEditorDelegate,
)
from picard.util import (
    IgnoreUpdatesContext as IgnoreUpdatesContext,
    format_time as format_time,
    icontheme as icontheme,
    restore_method as restore_method,
    thread as thread,
    throttle as throttle,
)
from picard.util.preservedtags import PreservedTags as PreservedTags
from picard.util.tags import display_tag_name as display_tag_name

class TagStatus:
    NONE: int
    NOCHANGE: int
    ADDED: int
    REMOVED: int
    CHANGED = ADDED | REMOVED
    EMPTY: int
    NOTREMOVABLE: int
    READONLY: int

class TagCounter(dict):
    parent: Incomplete
    counts: Incomplete
    different: Incomplete
    def __init__(self, parent) -> None: ...
    def __getitem__(self, tag): ...
    def add(self, tag, values) -> None: ...
    def display_value(self, tag): ...

class TagDiff:
    tag_names: Incomplete
    new: Incomplete
    orig: Incomplete
    status: Incomplete
    objects: int
    max_length_delta_ms: Incomplete
    def __init__(self, max_length_diff: int = 2) -> None: ...
    def add(
        self,
        tag,
        orig_values,
        new_values,
        removable,
        removed: bool = False,
        readonly: bool = False,
        top_tags: Incomplete | None = None,
    ) -> None: ...
    def tag_status(self, tag): ...

class TableTagEditorDelegate(TagEditorDelegate):
    def createEditor(self, parent, option, index): ...
    def sizeHint(self, option, index): ...
    def get_tag_name(self, index): ...

class MetadataBox(QtWidgets.QTableWidget):
    options: Incomplete
    COLUMN_ORIG: int
    COLUMN_NEW: int
    parent: Incomplete
    files: Incomplete
    tracks: Incomplete
    objects: Incomplete
    tag_diff: Incomplete
    selection_mutex: Incomplete
    selection_dirty: bool
    editing: Incomplete
    clipboard: Incomplete
    add_tag_action: Incomplete
    changes_first_action: Incomplete
    add_tag_shortcut: Incomplete
    edit_tag_shortcut: Incomplete
    remove_tag_shortcut: Incomplete
    preserved_tags: Incomplete
    ignore_updates: Incomplete
    def __init__(self, parent) -> None: ...
    def get_file_lookup(self): ...
    def lookup_tags(self): ...
    def open_link(self, values, tag) -> None: ...
    def edit(self, index, trigger, event): ...
    def keyPressEvent(self, event) -> None: ...
    def copy_value(self) -> None: ...
    def paste_value(self) -> None: ...
    def update_clipboard(self) -> None: ...
    def closeEditor(self, editor, hint) -> None: ...
    def contextMenuEvent(self, event) -> None: ...
    def edit_tag(self, tag) -> None: ...
    def edit_selected_tag(self) -> None: ...
    def toggle_changes_first(self, checked) -> None: ...
    def remove_tag(self, tag) -> None: ...
    def remove_selected_tags(self) -> None: ...
    def tag_is_removable(self, tag): ...
    def tag_is_editable(self, tag): ...
    def selected_tags(self, filter_func: Incomplete | None = None): ...
    def update(self, drop_album_caches: bool = False) -> None: ...
    def set_item_value(self, item, tags, name) -> None: ...
    def restore_state(self) -> None: ...
    def save_state(self) -> None: ...
