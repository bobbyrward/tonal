import wx
import sys
import wx.lib.mixins.listctrl as listmix
from tonal.util.uniquekey import UniqueKeyCollection

__all__ = [ 'EVT_PLAYLIST_ITEM_SELECTED'
          , 'EVT_PLAYLIST_ITEM_DOUBLECLICK'
          , 'PlaylistEvent'
          , 'PlaylistListCtrl'
          , 'PlaylistListCtrlPanel' 
          ]


# Fired when a playlist item is selected
_EVT_PLAYLIST_ITEM_SELECTED = wx.NewEventType()
EVT_PLAYLIST_ITEM_SELECTED = wx.PyEventBinder(_EVT_PLAYLIST_ITEM_SELECTED, 1)

# Fired when a playlist item is doubleclicked
_EVT_PLAYLIST_ITEM_DOUBLECLICK = wx.NewEventType()
EVT_PLAYLIST_ITEM_DOUBLECLICK = wx.PyEventBinder(_EVT_PLAYLIST_ITEM_DOUBLECLICK, 1)

class PlaylistEvent(wx.PyCommandEvent):
    def __init__(self, evtType, id):
        wx.PyCommandEvent.__init__(self, evtType, id)
        self.playlist_item = None

    def SetPlaylistItem(self, item):
        self.playlist_item = item

    def GetPlaylistItem(self):
        return self.playlist_item


class PlaylistListCtrl(wx.ListCtrl, listmix.ListCtrlAutoWidthMixin):
    def __init__(self, parent, style=0):
        wx.ListCtrl.__init__(self, parent, -1, style=style)
        listmix.ListCtrlAutoWidthMixin.__init__(self)

class PlaylistListCtrlPanel(wx.Panel): #, listmix.ColumnSorterMixin):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, style=wx.WANTS_CHARS)
        self._create_ui()
        self.itemcol = UniqueKeyCollection()
        self._setup_list()
#        listmix.ColumnSorterMixin.__init__(self)

    def _fire_playlist_event(self, evtType, item):
        evt = PlaylistEvent(evtType, self.GetId())
        evt.SetPlaylistItem(item)
        self.GetEventHandler().ProcessEvent(evt)

    def GetListCtrl(self):
        return self.list

    def _create_ui(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.list = PlaylistListCtrl(self, 
                style=wx.LC_REPORT|wx.BORDER_NONE|wx.LC_HRULES)
        sizer.Add(self.list, 1, wx.EXPAND)
        self.SetSizerAndFit(sizer)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self._on_item_activated, 
                self.list)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self._on_item_selected,
                self.list)
        self.Bind(wx.EVT_LIST_DELETE_ITEM, self._on_item_deleted,
                self.list)
        self.Bind(wx.EVT_LIST_DELETE_ALL_ITEMS, self._on_reset_list,
                self.list)

    def Reset(self):
        self.list.DeleteAllItems()

    def InsertPlaylistItem(self, playlist_item, idx=sys.maxint):
        md = playlist_item.metadata()
        if md is None:
            print 'Error: No metadata for "%s"' % playlist_item.filename
            return

        index = self.list.InsertStringItem(idx, md.title)

        key = self.itemcol.insert(playlist_item)
        self.list.SetItemData(index, key)

        if index == -1:
            raise RuntimeError('unable to add item to list')

        self.list.SetStringItem(index, 1, md.artist)
        self.list.SetStringItem(index, 2, md.album)
        self.list.SetStringItem(index, 3, str(md.trackno))
        self.list.SetStringItem(index, 4, md.genre)

    def _on_item_activated(self, evt):
        key = self.list.GetItemData(evt.GetIndex())
        playlist_item = self.itemcol.get(key)
        self._fire_playlist_event(_EVT_PLAYLIST_ITEM_DOUBLECLICK, playlist_item)
        evt.Skip()

    def _on_item_selected(self, evt):
        key = self.list.GetItemData(evt.GetIndex())
        playlist_item = self.itemcol.get(key)
        self._fire_playlist_event(_EVT_PLAYLIST_ITEM_SELECTED, playlist_item)
        evt.Skip()

    def _on_item_deleted(self, evt):
        key = self.list.GetItemData(evt.GetIndex())
        self.itemcol.remove(key)
        evt.Skip()

    def _on_reset_list(self, evt):
        self.itemcol.reset()
        evt.Skip()

    def _setup_list(self):
        self.list.InsertColumn(0, 'Title')
        self.list.InsertColumn(1, 'Artist')
        self.list.InsertColumn(2, 'Album')
        self.list.InsertColumn(3, '#')
        self.list.InsertColumn(4, 'Genre')

    def autosize(self):
        self.list.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(1, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(2, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(3, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(4, wx.LIST_AUTOSIZE)


    
