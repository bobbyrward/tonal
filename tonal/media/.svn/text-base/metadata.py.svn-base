from pyglet import media
from tonal.media import is_audio_file

__all__ = [ 'Metadata'
          , 'get_metadata'
          ]

class Metadata(object):
    def __init__(self, **kwargs):
        self.title    = kwargs.get('title', 'Unknown Title')
        self.artist   = kwargs.get('artist', 'Unknown Artist')
        self.album    = kwargs.get('album', 'Unknown Album')
        self.year     = kwargs.get('year', 0)
        self.trackno  = kwargs.get('trackno', 0)
        #TODO: Get a list of enumerated genres in decimal form
        self.genre    = kwargs.get('genre', 'Unknown Genre')
        self.duration = kwargs.get('duration', 0)

def get_metadata(filename, media_file = None):
    from metadata import Metadata
    if not media_file:
        media_file = media.load(filename)

    if not is_audio_file('', media_file):
        return None

    md = media_file.file_info

    return Metadata(title=md.title, artist=md.author, 
            album=md.album, year=md.year, 
            trackno=md.track, genre=md.genre,
            duration=md.duration
            )


