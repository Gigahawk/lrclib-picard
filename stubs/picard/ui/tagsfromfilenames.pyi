from _typeshed import Incomplete
from picard.config import TextOption as TextOption, get_config as get_config
from picard.script.parser import normalize_tagname as normalize_tagname
from picard.ui import PicardDialog as PicardDialog
from picard.ui.ui_tagsfromfilenames import (
    Ui_TagsFromFileNamesDialog as Ui_TagsFromFileNamesDialog,
)
from picard.ui.util import StandardButton as StandardButton
from picard.util.tags import display_tag_name as display_tag_name

class TagMatchExpression:
    replace_underscores: Incomplete
    def __init__(self, expression, replace_underscores: bool = False) -> None: ...
    @property
    def matched_tags(self): ...
    def match_file(self, filename): ...

class TagsFromFileNamesDialog(PicardDialog):
    help_url: str
    options: Incomplete
    ui: Incomplete
    files: Incomplete
    items: Incomplete
    def __init__(self, files, parent: Incomplete | None = None) -> None: ...
    def preview(self) -> None: ...
    def accept(self) -> None: ...
