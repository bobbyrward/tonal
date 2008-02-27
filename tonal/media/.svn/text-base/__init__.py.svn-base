from pyglet import options

# We set up the drivers like so 
# directsound first for windows, it's a given
# we eliminate openal because it's always choppy for me
# and finally no silent driver because it's better to 
# just bail if we can't play sound
options['audio'] = ('directsound', 'alsa') 

#options['debug_media'] = True

from pyglet import media

class MediaError(Exception):
    pass

def is_audio_file(filename, media_file = None):
    if not media_file:
        try:
            media_file = media.load(filename)
        except:
            return False

    if media_file.video_format:
        return False

    return (media_file.audio_format is not None)
    

