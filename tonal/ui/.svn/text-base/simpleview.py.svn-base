import wx
from tonal.playlists.simple import *
from tonal.ui.playlistctrl import *

class SimpleView(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        button_panel = wx.Panel(self)
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)

        def create_button(text, handler):
            b = wx.Button(button_panel, -1, text)
            button_sizer.Add(b, 0)
            self.Bind(wx.EVT_BUTTON, handler, b)

        create_button('Play', self._on_play)
        create_button('Stop', self._on_stop)
        create_button('Pause', self._on_pause)
        create_button('Open', self._on_open)

        button_panel.SetSizerAndFit(button_sizer)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(button_panel, 1, wx.EXPAND)
        self.playlist_panel = PlaylistListCtrlPanel(self)
        main_sizer.Add(self.playlist_panel, 1, wx.EXPAND)
        self.SetSizerAndFit(main_sizer)

        self.Bind(EVT_PLAYLIST_ITEM_DOUBLECLICK, 
                self._on_dblclick_item, self.playlist_panel)

    def _load_playlist(self, playlist):
        self.playlist = playlist
        self.playlist_panel.Reset()

        for item in self.playlist:
            print 'Adding item:', item.filename
            self.playlist_panel.InsertPlaylistItem(item)

        self.playlist_panel.autosize()

    def _on_dblclick_item(self, evt):
        item = evt.GetPlaylistItem()
        self._open(item.filename)
        self._on_play()

    def _on_play(self, evt = None):
        print wx.GetApp().player._filename
        wx.GetApp().player.play()

    def _on_pause(self, evt = None):
        wx.GetApp().player.pause()

    def _on_stop(self, evt = None):
        wx.GetApp().player.stop()

    def _open(self, filename):
        wx.GetApp().player.open(filename)

    def _on_open(self, evt = None):
        wildcard = 'All Supported Media Types|*.mp3;*.ogg;*.flac;*.ac3;*.wav;*.wma|'\
                   'Playlists (*.pls)|*.pls|' \
                   'All Files (*.*)|*.*'

        dlg = wx.FileDialog(self, wildcard = wildcard, style=wx.OPEN)
        if wx.ID_OK != dlg.ShowModal():
            return

        fname = dlg.GetPath()

        if fname.endswith('.pls'):
            self._load_playlist(playlist_from_pls(fname))
        else:
            self._open(dlg.GetPath())


