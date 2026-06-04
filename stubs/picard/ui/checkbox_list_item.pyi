from PyQt5.QtWidgets import QListWidgetItem
from _typeshed import Incomplete

class CheckboxListItem(QListWidgetItem):
    data: Incomplete
    def __init__(
        self, text: str = "", checked: bool = False, data: Incomplete | None = None
    ) -> None: ...
    @property
    def checked(self): ...
