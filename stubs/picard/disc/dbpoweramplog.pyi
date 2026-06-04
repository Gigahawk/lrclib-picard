from _typeshed import Incomplete
from collections.abc import Generator
from picard.disc.utils import (
    NotSupportedTOCError as NotSupportedTOCError,
    TocEntry as TocEntry,
    calculate_mb_toc_numbers as calculate_mb_toc_numbers,
)
from picard.util import detect_file_encoding as detect_file_encoding

RE_TOC_ENTRY: Incomplete

def filter_toc_entries(lines) -> Generator[Incomplete]: ...
def toc_from_file(path): ...
