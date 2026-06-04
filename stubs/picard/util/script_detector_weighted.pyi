from _typeshed import Incomplete
from enum import IntEnum

class ScriptSelectionOrder(IntEnum):
    SPECIFIED = 0
    WEIGHTED = 1

SCRIPT_WEIGHTING_FACTORS: Incomplete

def detect_script_weighted(string_to_check, threshold: float = 0.0): ...
def list_script_weighted(string_to_check, threshold: float = 0.0): ...
