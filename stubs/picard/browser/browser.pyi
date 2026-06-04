from PyQt5 import QtCore
from _typeshed import Incomplete
from http.server import BaseHTTPRequestHandler, HTTPServer
from picard import (
    PICARD_APP_NAME as PICARD_APP_NAME,
    PICARD_ORG_NAME as PICARD_ORG_NAME,
    PICARD_VERSION_STR as PICARD_VERSION_STR,
    log as log,
)
from picard.browser import addrelease as addrelease
from picard.config import get_config as get_config
from picard.oauth import OAuthInvalidStateError as OAuthInvalidStateError
from picard.util import mbid_validate as mbid_validate
from picard.util.thread import to_main as to_main
from socketserver import ThreadingMixIn

class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads: bool

SERVER_VERSION: Incomplete
RE_VALID_ORIGINS: Incomplete

class BrowserIntegration(QtCore.QObject):
    listen_port_changed: Incomplete
    server: Incomplete
    def __init__(self, parent: Incomplete | None = None) -> None: ...
    @property
    def host_address(self): ...
    @property
    def port(self): ...
    @property
    def is_running(self): ...
    def start(self) -> None: ...
    def stop(self) -> None: ...

class RequestHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self) -> None: ...
    def do_GET(self) -> None: ...
    def log_error(self, format, *args) -> None: ...
    def log_message(self, format, *args) -> None: ...
