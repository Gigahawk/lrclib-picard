from _typeshed import Incomplete
from picard import log as log
from picard.config import Option as Option, get_config as get_config
from picard.mbjson import (
    artist_credit_from_node as artist_credit_from_node,
    label_info_from_node as label_info_from_node,
    release_dates_and_countries_from_node as release_dates_and_countries_from_node,
)
from picard.ui import PicardDialog as PicardDialog
from picard.ui.ui_cdlookup import Ui_Dialog as Ui_Dialog
from picard.util import (
    compare_barcodes as compare_barcodes,
    restore_method as restore_method,
)

class CDLookupDialog(PicardDialog):
    dialog_header_state: str
    options: Incomplete
    releases: Incomplete
    disc: Incomplete
    ui: Incomplete
    def __init__(self, releases, disc, parent: Incomplete | None = None) -> None: ...
    def accept(self) -> None: ...
    def lookup(self) -> None: ...
    def restore_header_state(self) -> None: ...
    def save_header_state(self) -> None: ...
