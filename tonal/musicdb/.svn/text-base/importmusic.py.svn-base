from __future__ import with_statement

import os
import os.path
from datetime import datetime
from fnmatch import fnmatch
from tonal.media.metadata import get_metadata
from tonal.util.processdir import processdir
from tonal.musicdb.db import *

extensions = [ '*.mp3'
             , '*.ogg'
             , '*.wma'
             #, '*.m4a'
             #, '*.wav'
             , '*.flac'
             ]

def import_file(filename):
    print 'Processing %s' % filename
    #TODO: Use a transaction here to roll back on exception
    try:
        md = get_metadata(filename)

        if not md:
            return

        genre = md.genre  and get_or_create_genre(md.genre)   or None
        artist = md.artist and get_or_create_artist(md.artist) or None
        album = md.album  and get_or_create_album(md.album)   or None

        song   = Song()
        song.path = filename
        song.genre = genre
        song.artist = artist
        song.album = album
        album.artist = artist

        if md.title:
            song.title = md.title

        if md.year:
            song.year = md.year

        if md.trackno:
            song.track = md.trackno

        if md.duration:
            song.length = md.duration

        song.modified = os.path.getmtime(filename)
        song.size = os.path.getsize(filename)
        song.playcount = 0
        song.user_rating = 2.5
        song.time_added = datetime.now()
        song.blacklisted = False

        session.save(song)
        session.flush()
    except:
        pass

def import_dir(dir):
    processdir(dir, extensions, import_file)

def main():
    import sys

    directory = '.'

    if len(sys.argv) > 1:
        directory = sys.argv[1]

    import_dir(directory)

if __name__ == '__main__':
    main()






