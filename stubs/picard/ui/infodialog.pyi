from PyQt5 import QtWidgets
from _typeshed import Incomplete
from picard import log as log
from picard.album import Album as Album
from picard.coverart.image import CoverArtImageIOError as CoverArtImageIOError
from picard.file import File as File
from picard.track import Track as Track
from picard.ui import PicardDialog as PicardDialog
from picard.ui.colors import interface_colors as interface_colors
from picard.ui.ui_infodialog import Ui_InfoDialog as Ui_InfoDialog
from picard.ui.util import StandardButton as StandardButton
from picard.util import (
    bytes2human as bytes2human,
    encode_filename as encode_filename,
    format_time as format_time,
    open_local_path as open_local_path,
    union_sorted_lists as union_sorted_lists,
)

class ArtworkCoverWidget(QtWidgets.QWidget):
    SIZE: int
    def __init__(
        self,
        pixmap: Incomplete | None = None,
        text: Incomplete | None = None,
        parent: Incomplete | None = None,
    ) -> None: ...

class ArtworkTable(QtWidgets.QTableWidget):
    display_existing_art: Incomplete
    def __init__(self, display_existing_art) -> None: ...

class InfoDialog(PicardDialog):
    obj: Incomplete
    images: Incomplete
    existing_images: Incomplete
    ui: Incomplete
    display_existing_artwork: bool
    artwork_table: Incomplete
    def __init__(self, obj, parent: Incomplete | None = None) -> None: ...
    def tab_hide(self, widget) -> None: ...
    def show_item(self, item) -> None: ...

def format_file_info(file_): ...
def format_tracklist(cluster): ...
def text_as_html(text): ...

class FileInfoDialog(InfoDialog):
    def __init__(self, file_, parent: Incomplete | None = None) -> None: ...

class AlbumInfoDialog(InfoDialog):
    def __init__(self, album, parent: Incomplete | None = None) -> None: ...

class TrackInfoDialog(InfoDialog):
    def __init__(self, track, parent: Incomplete | None = None) -> None: ...

class ClusterInfoDialog(InfoDialog):
    def __init__(self, cluster, parent: Incomplete | None = None) -> None: ...
