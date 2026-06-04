from PyQt5 import QtWidgets
from picard import log as log
from picard.album import Album as Album
from picard.cluster import Cluster as Cluster, ClusterList as ClusterList
from picard.script import ScriptError as ScriptError, ScriptParser as ScriptParser
from picard.track import Track as Track
from picard.util import iter_unique as iter_unique

class ScriptsMenu(QtWidgets.QMenu):
    def __init__(self, scripts, *args) -> None: ...
