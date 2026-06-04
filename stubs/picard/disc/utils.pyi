from _typeshed import Incomplete
from typing import NamedTuple

PREGAP_LENGTH: int
DATA_TRACK_GAP: int

class TocEntry(NamedTuple):
    number: Incomplete
    start_sector: Incomplete
    end_sector: Incomplete

class NotSupportedTOCError(Exception): ...

def calculate_mb_toc_numbers(toc): ...
