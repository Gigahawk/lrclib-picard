from _typeshed import Incomplete
from picard.config import get_config as get_config
from picard.ui import PicardDialog as PicardDialog
from picard.ui.ui_passworddialog import Ui_PasswordDialog as Ui_PasswordDialog

class PasswordDialog(PicardDialog):
    ui: Incomplete
    def __init__(
        self, authenticator, reply, parent: Incomplete | None = None
    ) -> None: ...
    def set_new_password(self) -> None: ...

class ProxyDialog(PicardDialog):
    ui: Incomplete
    def __init__(
        self, authenticator, proxy, parent: Incomplete | None = None
    ) -> None: ...
    def set_proxy_password(self) -> None: ...
