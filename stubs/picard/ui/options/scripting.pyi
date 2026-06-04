from _typeshed import Incomplete
from picard import log as log
from picard.config import (
    BoolOption as BoolOption,
    IntOption as IntOption,
    ListOption as ListOption,
    get_config as get_config,
)
from picard.const.sys import IS_MACOS as IS_MACOS
from picard.script import ScriptParser as ScriptParser
from picard.script.serializer import (
    ScriptImportExportError as ScriptImportExportError,
    TaggingScript as TaggingScript,
)
from picard.ui import PicardDialog as PicardDialog, SingletonDialog as SingletonDialog
from picard.ui.moveable_list_view import MoveableListView as MoveableListView
from picard.ui.options import (
    OptionsCheckError as OptionsCheckError,
    OptionsPage as OptionsPage,
    register_options_page as register_options_page,
)
from picard.ui.ui_options_script import (
    Ui_ScriptingOptionsPage as Ui_ScriptingOptionsPage,
)
from picard.ui.ui_scripting_documentation_dialog import (
    Ui_ScriptingDocumentationDialog as Ui_ScriptingDocumentationDialog,
)
from picard.ui.util import qlistwidget_items as qlistwidget_items
from picard.ui.widgets.scriptdocumentation import (
    ScriptingDocumentationWidget as ScriptingDocumentationWidget,
)
from picard.ui.widgets.scriptlistwidget import (
    ScriptListWidgetItem as ScriptListWidgetItem,
)

class ScriptCheckError(OptionsCheckError): ...
class ScriptFileError(OptionsCheckError): ...

class ScriptingDocumentationDialog(PicardDialog, SingletonDialog):
    defaultsize: Incomplete
    parent: Incomplete
    ui: Incomplete
    def __init__(self, parent) -> None: ...
    def closeEvent(self, event) -> None: ...

class ScriptingOptionsPage(OptionsPage):
    NAME: str
    TITLE: Incomplete
    PARENT: Incomplete
    SORT_ORDER: int
    ACTIVE: bool
    HELP_URL: str
    options: Incomplete
    default_script_directory: Incomplete
    default_script_extension: str
    ui: Incomplete
    move_view: Incomplete
    FILE_TYPE_ALL: Incomplete
    FILE_TYPE_SCRIPT: Incomplete
    FILE_TYPE_PACKAGE: Incomplete
    def __init__(self, parent: Incomplete | None = None) -> None: ...
    def show_scripting_documentation(self) -> None: ...
    def output_error(self, title, fmt, params) -> None: ...
    def output_file_error(self, error: ScriptImportExportError): ...
    def import_script(self) -> None: ...
    def export_script(self) -> None: ...
    def enable_tagger_scripts_toggled(self, on) -> None: ...
    def script_selected(self) -> None: ...
    def live_update_and_check(self) -> None: ...
    def reset_selected_item(self) -> None: ...
    def check(self) -> None: ...
    def restore_defaults(self) -> None: ...
    def load(self) -> None: ...
    def save(self) -> None: ...
    def display_error(self, error) -> None: ...
