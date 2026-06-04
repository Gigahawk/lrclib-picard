from PyQt5 import QtCore
from PyQt5.QtNetwork import QNetworkRequest
from _typeshed import Incomplete
from picard import (
    PICARD_APP_NAME as PICARD_APP_NAME,
    PICARD_ORG_NAME as PICARD_ORG_NAME,
    PICARD_VERSION_STR as PICARD_VERSION_STR,
    log as log,
)
from picard.config import get_config as get_config
from picard.const import CACHE_SIZE_IN_BYTES as CACHE_SIZE_IN_BYTES, appdirs as appdirs
from picard.oauth import OAuthManager as OAuthManager
from picard.util import (
    build_qurl as build_qurl,
    bytes2human as bytes2human,
    encoded_queryargs as encoded_queryargs,
    parse_json as parse_json,
)
from picard.util.xml import parse_xml as parse_xml
from picard.webservice import ratecontrol as ratecontrol
from picard.webservice.utils import port_from_qurl as port_from_qurl
from typing import NamedTuple

COUNT_REQUESTS_DELAY_MS: int
TEMP_ERRORS_RETRIES: int
USER_AGENT_STRING: Incomplete
CLIENT_STRING: Incomplete
DEFAULT_RESPONSE_PARSER_TYPE: str

class Parser(NamedTuple):
    mimetype: Incomplete
    parser: Incomplete

class UnknownResponseParserError(Exception):
    def __init__(self, response_type) -> None: ...

class WSRequest(QNetworkRequest):
    response_mimetype: Incomplete
    response_parser: Incomplete
    method: Incomplete
    handler: Incomplete
    parse_response_type: Incomplete
    request_mimetype: Incomplete
    data: Incomplete
    cacheloadcontrol: Incomplete
    refresh: Incomplete
    priority: Incomplete
    important: Incomplete
    def __init__(
        self,
        *,
        method: Incomplete | None = None,
        handler: Incomplete | None = None,
        parse_response_type: Incomplete | None = None,
        data: Incomplete | None = None,
        mblogin: bool = False,
        cacheloadcontrol: Incomplete | None = None,
        refresh: bool = False,
        priority: bool = False,
        important: bool = False,
        request_mimetype: Incomplete | None = None,
        url: Incomplete | None = None,
        queryargs: Incomplete | None = None,
        unencoded_queryargs: Incomplete | None = None,
    ) -> None: ...
    @property
    def has_auth(self): ...
    @property
    def host(self): ...
    @property
    def port(self): ...
    @property
    def path(self): ...
    @property
    def access_token(self): ...
    @access_token.setter
    def access_token(self, access_token) -> None: ...
    @property
    def mblogin(self): ...
    @mblogin.setter
    def mblogin(self, mblogin) -> None: ...
    def get_host_key(self): ...
    def max_retries_reached(self): ...
    def mark_for_retry(self, important: bool = True, priority: bool = True): ...

class RequestTask(
    NamedTuple(
        "RequestTask",
        [("hostkey", Incomplete), ("func", Incomplete), ("priority", Incomplete)],
    )
):
    @staticmethod
    def from_request(request, func): ...

class RequestPriorityQueue:
    def __init__(self, ratecontrol) -> None: ...
    def count(self): ...
    def add_task(self, task, important: bool = False): ...
    def remove_task(self, task) -> None: ...
    def run_ready_tasks(self): ...

class WebService(QtCore.QObject):
    PARSERS: Incomplete
    manager: Incomplete
    oauth_manager: Incomplete
    def __init__(self, parent: Incomplete | None = None) -> None: ...
    def ssl_errors(self, reply, errors) -> None: ...
    @staticmethod
    def http_response_code(reply): ...
    @staticmethod
    def http_response_phrase(reply): ...
    @staticmethod
    def display_url(url): ...
    def set_cache(self, cache_size_in_bytes: Incomplete | None = None) -> None: ...
    def setup_proxy(self) -> None: ...
    def set_transfer_timeout(self, timeout) -> None: ...
    @staticmethod
    def urls_equivalent(leftUrl, rightUrl): ...
    def get(
        self,
        host,
        port,
        path,
        handler,
        parse_response_type=...,
        priority: bool = False,
        important: bool = False,
        mblogin: bool = False,
        cacheloadcontrol: Incomplete | None = None,
        refresh: bool = False,
        queryargs: Incomplete | None = None,
    ): ...
    def post(
        self,
        host,
        port,
        path,
        data,
        handler,
        parse_response_type=...,
        priority: bool = False,
        important: bool = False,
        mblogin: bool = True,
        queryargs: Incomplete | None = None,
        request_mimetype: Incomplete | None = None,
    ): ...
    def put(
        self,
        host,
        port,
        path,
        data,
        handler,
        priority: bool = True,
        important: bool = False,
        mblogin: bool = True,
        queryargs: Incomplete | None = None,
        request_mimetype: Incomplete | None = None,
    ): ...
    def delete(
        self,
        host,
        port,
        path,
        handler,
        priority: bool = True,
        important: bool = False,
        mblogin: bool = True,
        queryargs: Incomplete | None = None,
    ): ...
    def download(
        self,
        host,
        port,
        path,
        handler,
        priority: bool = False,
        important: bool = False,
        cacheloadcontrol: Incomplete | None = None,
        refresh: bool = False,
        queryargs: Incomplete | None = None,
    ): ...
    def get_url(self, **kwargs): ...
    def post_url(self, **kwargs): ...
    def put_url(self, **kwargs): ...
    def delete_url(self, **kwargs): ...
    def download_url(self, **kwargs): ...
    def stop(self) -> None: ...
    def add_task(self, func, request): ...
    def add_request(self, request): ...
    def remove_task(self, task) -> None: ...
    @classmethod
    def add_parser(cls, response_type, mimetype, parser) -> None: ...
    @classmethod
    def get_response_mimetype(cls, response_type): ...
    @classmethod
    def get_response_parser(cls, response_type): ...
