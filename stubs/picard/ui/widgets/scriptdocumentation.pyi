from PyQt5 import QtWidgets
from _typeshed import Incomplete
from picard.const import PICARD_URLS as PICARD_URLS
from picard.script import (
    script_function_documentation_all as script_function_documentation_all,
)
from picard.ui import FONT_FAMILY_MONOSPACE as FONT_FAMILY_MONOSPACE
from picard.ui.theme import theme as theme

DOCUMENTATION_HTML_TEMPLATE: str

class ScriptingDocumentationWidget(QtWidgets.QWidget):
    verticalLayout: Incomplete
    textBrowser: Incomplete
    horizontalLayout: Incomplete
    scripting_doc_link: Incomplete
    def __init__(self, parent, include_link: bool = True, *args, **kwargs) -> None: ...
