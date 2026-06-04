from _typeshed import Incomplete
from picard.const import PICARD_URLS as PICARD_URLS
from picard.formats import supported_extensions as supported_extensions
from picard.ui import PicardDialog as PicardDialog, SingletonDialog as SingletonDialog
from picard.ui.ui_aboutdialog import Ui_AboutDialog as Ui_AboutDialog
from picard.util import versions as versions

class AboutDialog(PicardDialog, SingletonDialog):
    ui: Incomplete
    def __init__(self, parent: Incomplete | None = None) -> None: ...
