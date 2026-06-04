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

import sys
import os
from typing import Union, List

# HACK: Picard (at least on Windows) seems to be missing some stuff from
# python stdlib
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "vendor"))

from picard import log
from picard.ui.itemviews import (
    BaseAction,
    register_track_action,
    register_album_action,
    register_file_action,
)
from picard.track import Track
from picard.album import Album
from picard.file import File

from .lrclib_py import LrcLib
from .util import flatten_to_files


def get_client():
    client = LrcLib()
    return client


class LrcLibLyricsGet(BaseAction):
    NAME = "Test Action"

    def callback(self, objs: List[Union[Album, Track, File]]):
        files = flatten_to_files(objs)
        for obj in files:
            if isinstance(obj, Album):
                log.info(f"Album: {obj}, {obj.metadata.get('title')}")
            elif isinstance(obj, Track):
                log.info(f"Track: {obj}, {obj.metadata.get('title')}")
            elif isinstance(obj, File):
                log.info(f"File: {obj}, {obj.filename}")


register_album_action(LrcLibLyricsGet())
register_track_action(LrcLibLyricsGet())
register_file_action(LrcLibLyricsGet())
