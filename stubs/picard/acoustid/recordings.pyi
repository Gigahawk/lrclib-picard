from _typeshed import Incomplete
from picard.acoustid.json_helpers import (
    parse_recording as parse_recording,
    recording_has_metadata as recording_has_metadata,
)
from picard.webservice import WebService as WebService
from picard.webservice.api_helpers import MBAPIHelper as MBAPIHelper
from typing import NamedTuple

SOURCE_THRESHOLD_NO_METADATA: float
MAX_NO_METADATA_RECORDINGS: int

class Recording:
    recording: dict
    result_score: float
    sources: int
    def __init__(
        self, recording, result_score: float = 1.0, sources: int = 1
    ) -> None: ...

class IncompleteRecording(NamedTuple):
    mbid: Incomplete
    acoustid: Incomplete
    result_score: Incomplete
    sources: Incomplete

class RecordingResolver:
    def __init__(self, ws: WebService, doc: dict, callback: callable) -> None: ...
    def resolve(self) -> None: ...

def get_score(node): ...
def parse_recording_map(recording_map: dict[str, dict[str, Recording]]): ...
def max_source_count(recordings: list[Recording]): ...
def max_source_count_raw_recording(recordings: list[dict]): ...
