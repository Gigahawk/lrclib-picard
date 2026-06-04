from _typeshed import Incomplete

class MoveableListView:
    list_widget: Incomplete
    up_button: Incomplete
    down_button: Incomplete
    update_callback: Incomplete
    def __init__(
        self, list_widget, up_button, down_button, callback: Incomplete | None = None
    ) -> None: ...
    def move_item(self, offset) -> None: ...
    def update_buttons(self) -> None: ...
