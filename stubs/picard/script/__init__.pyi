from _typeshed import Incomplete
from collections.abc import Generator
from picard import log as log
from picard.config import get_config as get_config
from picard.const import (
    DEFAULT_FILE_NAMING_FORMAT as DEFAULT_FILE_NAMING_FORMAT,
    DEFAULT_NAMING_PRESET_ID as DEFAULT_NAMING_PRESET_ID,
)
from picard.script.functions import (
    register_script_function as register_script_function,
    script_function as script_function,
)
from picard.script.parser import (
    MultiValue as MultiValue,
    ScriptEndOfFile as ScriptEndOfFile,
    ScriptError as ScriptError,
    ScriptExpression as ScriptExpression,
    ScriptFunction as ScriptFunction,
    ScriptParseError as ScriptParseError,
    ScriptParser as ScriptParser,
    ScriptRuntimeError as ScriptRuntimeError,
    ScriptSyntaxError as ScriptSyntaxError,
    ScriptText as ScriptText,
    ScriptUnicodeError as ScriptUnicodeError,
    ScriptUnknownFunction as ScriptUnknownFunction,
    ScriptVariable as ScriptVariable,
)
from picard.script.serializer import FileNamingScript as FileNamingScript

class ScriptFunctionDocError(Exception): ...

def script_function_documentation(
    name,
    fmt,
    functions: Incomplete | None = None,
    postprocessor: Incomplete | None = None,
): ...
def script_function_names(
    functions: Incomplete | None = None,
) -> Generator[Incomplete, Incomplete]: ...
def script_function_documentation_all(
    fmt: str = "markdown",
    pre: str = "",
    post: str = "",
    postprocessor: Incomplete | None = None,
): ...
def enabled_tagger_scripts_texts(): ...
def get_file_naming_script(settings): ...
def get_file_naming_script_presets() -> Generator[Incomplete, None, Incomplete]: ...
