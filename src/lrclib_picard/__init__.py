# ruff: noqa: E402
PLUGIN_NAME = "LRCLIB Picard"
PLUGIN_AUTHOR = "Gigahawk"
PLUGIN_DESCRIPTION = """
Automatically pull in lyric data from LRCLIB
"""

PLUGIN_LICENSE = "MIT"
PLUGIN_LICENSE_URL = "https://spdx.org/licenses/MIT.html"
PLUGIN_VERSION = "2.2.3"
PLUGIN_API_VERSIONS = ["2.0", "2.1", "2.2", "2.3", "2.4", "2.5", "2.6", "2.7"]

from picard import log
from picard.ui.itemviews import (
    BaseAction,
    register_track_action,
)

from .lrclib_py import LrcLib


def get_client():
    client = LrcLib()
    return client


class LrcLibLyricsGet(BaseAction):
    NAME = "Test Action"

    def callback(self, objs):
        import traceback

        log.info("=====OBJS")
        log.info(objs)
        log.info("======TRACEBACK")
        log.info(traceback.format_stack())


register_track_action(LrcLibLyricsGet())
