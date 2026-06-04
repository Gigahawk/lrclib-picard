from _typeshed import Incomplete
from enum import IntEnum
from picard.const import MB_ATTRIBUTES as MB_ATTRIBUTES

CAA_TYPES: Incomplete
CAA_TYPES_TR: Incomplete

def translate_caa_type(name): ...

class Id3ImageType(IntEnum):
    OTHER = 0
    FILE_ICON = 1
    FILE_ICON_OTHER = 2
    COVER_FRONT = 3
    COVER_BACK = 4
    LEAFLET_PAGE = 5
    MEDIA = 6
    LEAD_ARTIST = 7
    ARTIST = 8
    CONDUCTOR = 9
    BAND = 10
    COMPOSER = 11
    LYRICIST = 12
    RECORDING_DURATION = 13
    DURING_RECORDING = 14
    DURING_PERFORMANCE = 15
    VIDEO_SCREEN_CAPTURE = 16
    BRIGHT_COLOURED_FISH = 17
    ILLUSTRATION = 18
    LOGO_ARTIST = 19
    LOGO_STUDIO = 20

def image_type_from_id3_num(id3type): ...
def image_type_as_id3_num(texttype): ...
def types_from_id3(id3type): ...
