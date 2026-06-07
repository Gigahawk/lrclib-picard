from typing import Union, Iterable, List

from picard.track import Track
from picard.album import Album
from picard.file import File

_item = Union[Album, Track, File]


def flatten_to_files(objs: Union[Iterable[_item], _item]) -> List[File]:
    if not isinstance(objs, Iterable):
        objs = [objs]
    out = []
    for obj in objs:
        if isinstance(obj, File):
            out.append(obj)
        elif isinstance(obj, Track):
            if obj.linked_files:
                out.extend(obj.linked_files)
        elif isinstance(obj, Album):
            for track in obj.tracks:
                if track.linked_files:
                    out.extend(track.linked_files)
    return out


def set_lyrics(file: File, lyrics: str, tag_names: Iterable[str] = ["lyrics"]):
    for t in tag_names:
        file.metadata[t] = lyrics
    file.save()
