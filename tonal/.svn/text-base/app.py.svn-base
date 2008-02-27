import wx
from tonal.media.musicplayer import MusicPlayer
from tonal.ui.main_frame import TonalMainFrame
from tonal import settings 

class TonalApp(wx.App):
    def _get_player(self):
        return self._music_player
    player = property(fget=_get_player)

    def _get_main_frame(self):
        return self._main_frame
    main_frame = property(fget=_get_main_frame)

    def _get_user_app_data_dir():
        return settings.get_user_app_data_dir()
    user_app_data_dir = property(fget=_get_user_app_data_dir)
        
    def OnInit(self):
        settings.ensure_app_dirs_exists()
        self._music_player = MusicPlayer()
        self._main_frame = TonalMainFrame()
        self._main_frame.Show(True)
        self.SetTopWindow(self._main_frame)
        return True

def run():
    app = TonalApp()
    app.MainLoop()

if __name__ == '__main__':
    run()

