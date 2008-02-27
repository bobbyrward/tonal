from pyglet import media
from tonal.media import MediaError, is_audio_file
from tonal.media.metadata import get_metadata

_MEDIA_DISPATCH_INTERVAL = 0.01

class MusicPlayer(object):
    def __init__(self):
        from threading import Thread, Lock
        self._quit = False
        self._mutex = Lock()
        self._metadata = None
        self._filename = None
        self._song = None
        self._player = None
        self._thread = Thread(target=self._dispatch_events)
        self._thread.start()

    def metadata(self):
        return self._metadata

    def shutdown(self):
        self._quit = True
        if self._thread:
            self._thread.join()
            self._thread = None

    def __del__(self):
        self.shutdown()

    def open(self, filename):
        song = media.load(filename)

        if not is_audio_file('', song):
            raise MediaError('File "%s" is not an audio or audio only file' % filename)

        playing = False
        if self._player and self._player.playing:
            playing = True

        self.stop()

        self._lock()
        try:
            self._player = None
        finally:
            self._unlock()

        self._filename = filename
        self._song = song
        self._metadata = get_metadata('', song)

        if playing:
            self.play()

    def _on_eos(self):
        self._lock()
        self._player = None
        self._unlock()

    def play(self):
        if self._player and not self._player.playing:
            self._lock()
            try:
                self._player.play()
            finally:
                self._unlock()
        elif not self._player and self._song:
            self.open(self._filename)
            self._lock()
            try:
                self._player = self._song.play()
                self._player.on_eos = self._on_eos
            finally:
                self._unlock()

    def pause(self):
        if self._player and self._player.playing:
            self._lock()
            try:
                self._player.pause()
            finally:
                self._unlock()

    def stop(self):
        if self._player:
            self._lock()
            try: 
                self._player.stop()
                self._player = None
            except: 
                pass
            finally:
                self._unlock()

    def _lock(self):
        self._mutex.acquire()

    def _unlock(self):
        self._mutex.release()

    def _dispatch_events(self):
        from time import sleep
        while not self._quit:
            self._lock()
            try:
                media.dispatch_events()
            finally:
                self._unlock()
            sleep(_MEDIA_DISPATCH_INTERVAL)

