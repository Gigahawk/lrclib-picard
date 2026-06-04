from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from picard import PICARD_APP_ID as PICARD_APP_ID, log as log
from picard.const.sys import (
    IS_HAIKU as IS_HAIKU,
    IS_MACOS as IS_MACOS,
    IS_WIN as IS_WIN,
)
from picard.util import sanitize_filename as sanitize_filename
from typing import Any, Iterable

class PipeError(Exception):
    MESSAGE: str
    messages: Incomplete
    def __init__(self, *messages) -> None: ...

class PipeErrorInvalidArgs(PipeError):
    MESSAGE: str

class PipeErrorInvalidAppData(PipeError):
    MESSAGE: str

class PipeErrorNotFound(PipeError):
    MESSAGE: str

class PipeErrorBroken(PipeError):
    MESSAGE: str

class PipeErrorInvalidResponse(PipeError):
    MESSAGE: str

class PipeErrorWin(PipeError):
    MESSAGE: str

class PipeErrorNoPermission(PipeError):
    MESSAGE: str

class PipeErrorNoDestination(PipeError):
    MESSAGE: str

class AbstractPipe(metaclass=ABCMeta):
    NO_RESPONSE_MESSAGE: str
    MESSAGE_TO_IGNORE: str
    TIMEOUT_SECS_WRITE: float
    @classmethod
    @property
    @abstractmethod
    def PIPE_DIRS(cls): ...
    path_was_forced: bool
    is_pipe_owner: bool
    pipe_running: bool
    unexpected_removal: bool
    path: Incomplete
    def __init__(
        self,
        app_name: str,
        app_version: str,
        args: Iterable[str] | None = None,
        forced_path: str | None = None,
        identifier: str | None = None,
    ) -> None: ...
    def read_from_pipe(self) -> list[str]: ...
    def send_to_pipe(self, message: str, timeout_secs: float | None = None) -> bool: ...
    def stop(self) -> None: ...

class UnixPipe(AbstractPipe):
    PIPE_DIRS: tuple[str]
    def __init__(
        self,
        app_name: str,
        app_version: str,
        args: Iterable[str] | None = None,
        forced_path: str | None = None,
        identifier: str | None = None,
    ) -> None: ...

class MacOSPipe(UnixPipe):
    PIPE_DIRS: tuple[str]

class HaikuPipe(UnixPipe):
    PIPE_DIRS: tuple[str]

class WinPipe(AbstractPipe):
    PIPE_DIRS: tuple[str]
    def __init__(
        self,
        app_name: str,
        app_version: str,
        args: Iterable[str] | None = None,
        forced_path: str | None = None,
        identifier: str | None = None,
    ) -> None: ...
    def stop(self) -> None: ...

Pipe: Any
Pipe = MacOSPipe
Pipe = HaikuPipe
Pipe = UnixPipe
