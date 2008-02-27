from __future__ import with_statement

from tonal.playlists import Playlist, PlaylistItem
from tonal.media.metadata import get_metadata

__all__ = [ 'playlist_from_list'
          , 'playlist_from_pls'
          , 'SimplePlaylistItem'
          , 'SimplePlaylist'
          ]

class SimplePlaylistItem(PlaylistItem):
    def __init__(self, filename):
        self._filename = filename
        self._metadata = None

    def _get_filename(self):
        return self._filename

    filename = property(fget=_get_filename)

    def metadata(self, refresh=False):
        if not self._metadata or refresh:
            self._metadata = get_metadata(self.filename)
        return self._metadata


class SimplePlaylist(Playlist):
    def __init__(self):
        self._items = []

    def at(self, idx):
        return self._items[idx]

    def remove(self, idx):
        return self._items[idx]

    def _check_type(self, item):
        if not isinstance(item, PlaylistItem):
            raise TypeError('Can only insert PlaylistItems into a SimplePlaylist')

    def insert(self, idx, item):
        self._check_type(item)
        self._items.insert(idx, item)

    def append(self, item):
        self._check_type(item)
        self._items.append(item)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

def playlist_from_pls(fname):
    import os.path

    playlist = SimplePlaylist()

    with open(fname, 'r') as fd:
        for line in fd:
            line = line.strip()
            if not os.path.exists(line):
                print 'WARNING: Unable to open "%s"' % line
                continue
            playlist.append(SimplePlaylistItem(line))

    return playlist

def playlist_from_list(files):
    import os.path

    playlist = SimplePlaylist()

    for file in files:
        if not os.path.exists(file):
            raise IOError('File "%s" does not exist' % file)

        playlist.append(SimplePlaylistItem(file))

    return playlist


        



        


