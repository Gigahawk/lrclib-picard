from PyQt5 import QtWidgets
from _typeshed import Incomplete
from collections.abc import Generator
from picard.config import get_config as get_config
from picard.const.sys import IS_MACOS as IS_MACOS, IS_WIN as IS_WIN
from picard.util import find_existing_path as find_existing_path

class StandardButton(QtWidgets.QPushButton):
    OK: int
    CANCEL: int
    HELP: int
    CLOSE: int
    def __init__(self, btntype) -> None: ...

def find_starting_directory(): ...

class MultiDirsSelectDialog(QtWidgets.QFileDialog):
    def __init__(self, *args) -> None: ...

def qlistwidget_items(qlistwidget) -> Generator[Incomplete]: ...
