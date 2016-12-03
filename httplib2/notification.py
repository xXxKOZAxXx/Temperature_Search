import wx, sys

app = wx.PySimpleApp()

class TestTaskBarIcon(wx.TaskBarIcon):

    def __init__(self):
        wx.TaskBarIcon.__init__(self)
        # create a test icon
        bmp = wx.EmptyBitmap(16, 16)
        dc = wx.MemoryDC(bmp)
        dc.SetBrush(wx.RED_BRUSH)
        dc.Clear()
        dc.SelectObject(wx.NullBitmap)

        testicon = wx.EmptyIcon()
        testicon.CopyFromBitmap(bmp)

        self.SetIcon(testicon)
        self.Bind(wx.EVT_TASKBAR_LEFT_UP, lambda e: (self.RemoveIcon(),sys.exit()))

        wx.NotificationMessage("", "Hello world!").Show()

icon = TestTaskBarIcon()
app.MainLoop()