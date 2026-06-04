from PyQt5.QtCore import QEvent, QRunnable
from _typeshed import Incomplete
from picard import log as log

class ProxyToMainEvent(QEvent):
    func: Incomplete
    args: Incomplete
    kwargs: Incomplete
    def __init__(self, func, *args, **kwargs) -> None: ...
    def run(self) -> None: ...

class Runnable(QRunnable):
    func: Incomplete
    next_func: Incomplete
    traceback: Incomplete
    def __init__(self, func, next_func, traceback: bool = True) -> None: ...
    def run(self) -> None: ...

def run_task(
    func,
    next_func: Incomplete | None = None,
    priority: int = 0,
    thread_pool: Incomplete | None = None,
    traceback: bool = True,
) -> None: ...
def to_main(func, *args, **kwargs) -> None: ...
def to_main_with_blocking(func, *args, **kwargs) -> None: ...
