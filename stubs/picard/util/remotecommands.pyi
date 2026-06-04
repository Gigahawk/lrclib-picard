from _typeshed import Incomplete
from picard import log as log

class RemoteCommand:
    method_name: Incomplete
    help_text: Incomplete
    help_args: Incomplete
    def __init__(
        self,
        method_name,
        help_text: Incomplete | None = None,
        help_args: Incomplete | None = None,
    ) -> None: ...

REMOTE_COMMANDS: Incomplete

class RemoteCommands:
    command_queue: Incomplete
    @classmethod
    def cmd_files_contains(cls, filepath: str): ...
    @classmethod
    def cmd_files_add(cls, filepath: str): ...
    @classmethod
    def cmd_files_remove(cls, filepath: str): ...
    @classmethod
    def has_quit(cls): ...
    @classmethod
    def set_quit(cls, value: bool): ...
    @classmethod
    def get_running(cls): ...
    @classmethod
    def set_running(cls, value: bool): ...
    @classmethod
    def parse_commands_to_queue(cls, commands) -> None: ...
    @classmethod
    def get_commands_from_file(cls, filepath: str): ...
