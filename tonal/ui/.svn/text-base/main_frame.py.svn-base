import wx
from tonal.ui.simpleview import SimpleView

class TonalMainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 
                'Tonal', size=(640, 480))

        self._create_ui()

    def _create_ui(self):
        self.Bind(wx.EVT_CLOSE, self._on_close)

        self.player_bar = wx.Panel(self)

        self.view = SimpleView(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.view, 1, wx.EXPAND)
        self.SetSizer(sizer)
        #self.Fit()

        self._create_menu()

    def _create_menu(self):
        menu_bar = wx.MenuBar()

        file_menu = wx.Menu()
        file_menu.Append(wx.ID_EXIT, 'E&xit', 'Exit the application')
        menu_bar.Append(file_menu, '&File')

        self.SetMenuBar(menu_bar)

    def _on_close(self, evt):
        wx.GetApp().player.shutdown()
        self.Destroy()


