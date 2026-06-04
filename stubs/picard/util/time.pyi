from _typeshed import Incomplete
from typing import NamedTuple

SECS_IN_DAY: int
SECS_IN_HOUR: int
SECS_IN_MINUTE: int

class Duration(NamedTuple):
    days: Incomplete
    hours: Incomplete
    minutes: Incomplete
    seconds: Incomplete

def euclidian_div(a, b): ...
def seconds_to_dhms(seconds): ...
def get_timestamp(seconds): ...
