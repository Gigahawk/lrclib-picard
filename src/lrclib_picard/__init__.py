PLUGIN_NAME = "LRCLIB Picard"
PLUGIN_AUTHOR = "Gigahawk"
PLUGIN_DESCRIPTION = """
Automatically pull in lyric data from LRCLIB
"""

PLUGIN_LICENSE = "MIT"
PLUGIN_LICENSE_URL = "https://spdx.org/licenses/MIT.html"
PLUGIN_VERSION = "2.2.3"
PLUGIN_API_VERSIONS = ["2.0", "2.1", "2.2", "2.3", "2.4", "2.5", "2.6", "2.7"]

from .lrclib_py import LrcLib  # noqa: E402


def get_client():
    client = LrcLib()
    return client
