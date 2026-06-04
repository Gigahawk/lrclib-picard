from _typeshed import Incomplete
from picard.config import Option as Option, get_config as get_config
from picard.file import File as File
from picard.mbjson import (
    countries_from_node as countries_from_node,
    recording_to_metadata as recording_to_metadata,
    release_group_to_metadata as release_group_to_metadata,
    release_to_metadata as release_to_metadata,
)
from picard.metadata import Metadata as Metadata
from picard.track import Track as Track
from picard.ui.searchdialog import Retry as Retry, SearchDialog as SearchDialog
from picard.util import (
    countries_shortlist as countries_shortlist,
    sort_by_similarity as sort_by_similarity,
)
from picard.webservice.api_helpers import build_lucene_query as build_lucene_query

class TrackSearchDialog(SearchDialog):
    dialog_header_state: str
    options: Incomplete
    file_: Incomplete
    columns: Incomplete
    def __init__(
        self, parent, force_advanced_search: Incomplete | None = None
    ) -> None: ...
    retry_params: Incomplete
    def search(self, text) -> None: ...
    def show_similar_tracks(self, file_) -> None: ...
    def retry(self) -> None: ...
    def handle_reply(self, document, http, error) -> None: ...
    def display_results(self) -> None: ...
    def parse_tracks(self, tracks) -> None: ...
    def accept_event(self, rows) -> None: ...
    def load_selection(self, row) -> None: ...
