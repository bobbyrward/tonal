import wx
import wx.lib.mixins.listctrl as listmix

ALBUM_ART_SIZE=(64,64)
PLAYER_PANEL_HEIGHT=96

class AlbumArtCtrl(wx.Window):
    def __init__(self, parent):
        wx.Window.__init__(self, parent, style=wx.BORDER_RAISED)
        self.SetClientSize(ALBUM_ART_SIZE)

        self.album_art = wx.Image('share/notes-128x128.png')
        self.bitmap = self.album_art.ConvertToBitmap()

        self.Bind(wx.EVT_PAINT, self._on_paint)

    def _on_paint(self, evt):
        dc = wx.PaintDC(self)
        gc = wx.GraphicsContext.Create(dc)
        gc.DrawBitmap(self.bitmap, *self.GetClientRect())

class PlaylistPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, style=wx.BORDER_SUNKEN)

        sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(self, label='Playlist', style=wx.BORDER_RAISED)
        sizer.Add(lbl, 0, wx.EXPAND)
        self.SetSizer(sizer)


#
# A little diagram to visualize the sizer grid
#
#X-------------------------------------
#-At-----------------------------------
#-Aa-----------------------------------
#-Ab-----------------------------------
#-A------------------------------------
#X-------------------------------------
#
# X = Spacer
# A = Album Art
# t = Title
# a = Artist
# b = Album
#
class PlayerPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetClientSize((10, PLAYER_PANEL_HEIGHT))
        self.SetMinSize((400, PLAYER_PANEL_HEIGHT))

        sizer = wx.GridBagSizer()

        album_art = AlbumArtCtrl(self)
        title = wx.StaticText(self, label='Title of the Song')
        artist = wx.StaticText(self, label='Artist\'s Name')
        album = wx.StaticText(self, label='The Album of Doom')

        large_font = wx.FFont(14, wx.FONTFAMILY_SWISS)
        small_font = wx.FFont(8, wx.FONTFAMILY_SWISS)

        title.SetFont(large_font)
        artist.SetFont(small_font)
        album.SetFont(small_font)

        sizer.Add((4, 4), (0, 0), (1, 1))
        sizer.Add(album_art, (1, 1), (4, 1))
        sizer.Add(title, (1, 3), (1, 3))
        sizer.Add(artist, (2, 3), (1, 3))
        sizer.Add(album, (3, 3), (1, 3))
        sizer.Add((4, 4), (5, 0), (1, 1))
        self.SetSizerAndFit(sizer)

class LibraryCategoryList(wx.ListCtrl, listmix.ListCtrlAutoWidthMixin):
    def __init__(self, parent, name):
        wx.ListCtrl.__init__(self, parent, 
                style=wx.LC_REPORT|wx.BORDER_SUNKEN|wx.LC_HRULES)
        listmix.ListCtrlAutoWidthMixin.__init__(self)
        self.InsertColumn(0, name)
        self.InsertColumn(1, 'Songs')
        self.SetColumnWidth(1, -2)
        self.SetMinSize((128, 128))
        self.setResizeColumn(1)

class LibraryGenreList(LibraryCategoryList):
    def __init__(self, parent):
        LibraryCategoryList.__init__(self, parent, 'Genre')

class LibraryAlbumList(LibraryCategoryList):
    def __init__(self, parent):
        LibraryCategoryList.__init__(self, parent, 'Album')

class LibraryArtistList(LibraryCategoryList):
    def __init__(self, parent):
        LibraryCategoryList.__init__(self, parent, 'Artist')

class LibrarySongList(wx.ListCtrl, listmix.ListCtrlAutoWidthMixin):
    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, 
                style=wx.LC_REPORT|wx.BORDER_SUNKEN|wx.LC_HRULES)
        listmix.ListCtrlAutoWidthMixin.__init__(self)
        self.InsertColumn(0, 'Title')
        self.InsertColumn(1, 'Artist')
        self.InsertColumn(2, 'Album')
        self.InsertColumn(3, '#')
        self.InsertColumn(4, 'Length')
        self.SetMinSize((128, 128))
        self.setResizeColumn(1)

class LibraryViewPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        sizer = wx.GridBagSizer()

        base_flags = wx.ALL|wx.EXPAND

        temp = LibraryGenreList(self)
        sizer.Add(temp, pos=(0, 0),
            flag=base_flags, border=5)

        temp = LibraryArtistList(self)
        sizer.Add(temp, pos=(0, 1), 
            flag=base_flags, border=5)

        temp = LibraryAlbumList(self)
        sizer.Add(temp, pos=(0, 2), 
            flag=base_flags, border=5)

        temp = LibrarySongList(self)
        sizer.Add(temp, pos=(1, 0), span=(1, 3), 
            flag=base_flags, border=5)

        sizer.AddGrowableCol(0)
        sizer.AddGrowableCol(1)
        sizer.AddGrowableCol(2)

        sizer.AddGrowableRow(0)
        sizer.AddGrowableRow(1)

        self.SetSizerAndFit(sizer)

class PlaylistsViewPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetMinSize((256, 256))
        self.SetBackgroundColour(wx.BLUE)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(wx.StaticText(self, label='Playlists'), 0, wx.EXPAND)
        self.SetSizer(sizer)

class FilesViewPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetMinSize((256, 256))
        self.SetBackgroundColour(wx.BLUE)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(wx.StaticText(self, label='Files'), 0, wx.EXPAND)
        self.SetSizer(sizer)

class ViewPanel(wx.Notebook):
    def __init__(self, parent):
        wx.Notebook.__init__(self, parent)
        self.library = LibraryViewPanel(self)
        self.playlists = PlaylistsViewPanel(self)
        self.files = FilesViewPanel(self)
        self.AddPage(self.library, 'Library')
        self.AddPage(self.playlists, 'Playlists')
        self.AddPage(self.files, 'Files')

class SidePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        sizer = wx.BoxSizer(wx.VERTICAL)
        player_panel = PlayerPanel(self)
        sizer.Add(player_panel, 0, wx.EXPAND)

        view_panel = ViewPanel(self)
        sizer.Add(view_panel, 1, wx.EXPAND)

        self.SetSizerAndFit(sizer)


class MockFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Mockup 1', size=(800, 600))

        sizer = wx.BoxSizer(wx.VERTICAL)

        splitter = wx.SplitterWindow(self)

        playlist_panel = PlaylistPanel(splitter)
        side_panel = SidePanel(splitter)
        
        splitter.SetMinimumPaneSize(256)
        splitter.SplitVertically(side_panel, playlist_panel, -256)

        sizer.Add(splitter, 1, wx.EXPAND)
        self.SetSizer(sizer)

        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        file_menu.Append(wx.ID_EXIT, 'E&xit')
        menu_bar.Append(file_menu, '&File')
        help_menu = wx.Menu()
        help_menu.Append(wx.ID_ABOUT, '&About')
        menu_bar.Append(help_menu, '&Help')
        self.SetMenuBar(menu_bar)


def main(argv=None):
    if not argv:
        import sys
        argv = sys.argv
    app = wx.PySimpleApp()
    frame = MockFrame()
    frame.Show(True)
    app.MainLoop()

if __name__ == '__main__':
    main()


