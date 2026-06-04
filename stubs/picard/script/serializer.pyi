from _typeshed import Incomplete
from enum import IntEnum
from picard import log as log
from picard.const import (
    DEFAULT_SCRIPT_NAME as DEFAULT_SCRIPT_NAME,
    SCRIPT_LANGUAGE_VERSION as SCRIPT_LANGUAGE_VERSION,
)
from picard.util import make_filename_from_title as make_filename_from_title

class PicardScriptType(IntEnum):
    BASE = 0
    TAGGER = 1
    FILENAMING = 2

class ScriptImportExportError(Exception):
    format: Incomplete
    filename: Incomplete
    error_msg: Incomplete
    def __init__(
        self,
        *args,
        format: Incomplete | None = None,
        filename: Incomplete | None = None,
        error_msg: Incomplete | None = None,
    ) -> None: ...

class ScriptImportError(Exception):
    def __init__(self, *args) -> None: ...

class MultilineLiteral(str):
    @staticmethod
    def yaml_presenter(dumper, data): ...

class PicardScript:
    TYPE: Incomplete
    OUTPUT_FIELDS: Incomplete
    title: Incomplete
    id: Incomplete
    last_updated: Incomplete
    script_language_version: Incomplete
    def __init__(
        self,
        script: str = "",
        title: str = "",
        id: Incomplete | None = None,
        last_updated: Incomplete | None = None,
        script_language_version: Incomplete | None = None,
    ) -> None: ...
    def __getitem__(self, setting): ...
    @property
    def script(self): ...
    @script.setter
    def script(self, value) -> None: ...
    @staticmethod
    def make_last_updated(): ...
    def update_last_updated(self) -> None: ...
    def update_script_setting(self, **kwargs) -> None: ...
    def update_from_dict(self, settings) -> None: ...
    def to_dict(self): ...
    def export_script(self, parent: Incomplete | None = None): ...
    @classmethod
    def import_script(cls, parent: Incomplete | None = None): ...
    @classmethod
    def create_from_dict(cls, script_dict, create_new_id: bool = True): ...
    def copy(self): ...
    def to_yaml(self): ...
    @classmethod
    def create_from_yaml(cls, yaml_string, create_new_id: bool = True): ...
    @property
    def filename(self): ...

class TaggingScript(PicardScript):
    TYPE: Incomplete
    OUTPUT_FIELDS: Incomplete
    def __init__(
        self,
        script: str = "",
        title: str = "",
        id: Incomplete | None = None,
        last_updated: Incomplete | None = None,
        script_language_version: Incomplete | None = None,
    ) -> None: ...

class FileNamingScript(PicardScript):
    TYPE: Incomplete
    OUTPUT_FIELDS: Incomplete
    author: Incomplete
    license: Incomplete
    version: Incomplete
    def __init__(
        self,
        script: str = "",
        title: str = "",
        id: Incomplete | None = None,
        author: str = "",
        description: str = "",
        license: str = "",
        version: str = "",
        last_updated: Incomplete | None = None,
        script_language_version: Incomplete | None = None,
        **kwargs,
    ) -> None: ...
    @property
    def description(self): ...
    @description.setter
    def description(self, value) -> None: ...
