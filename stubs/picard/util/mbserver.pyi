from _typeshed import Incomplete
from picard.config import get_config as get_config
from picard.const import MUSICBRAINZ_SERVERS as MUSICBRAINZ_SERVERS
from picard.util import build_qurl as build_qurl
from typing import NamedTuple

class ServerTuple(NamedTuple):
    host: Incomplete
    port: Incomplete

def is_official_server(host): ...
def get_submission_server(): ...
def build_submission_url(
    path: Incomplete | None = None, query_args: Incomplete | None = None
): ...
