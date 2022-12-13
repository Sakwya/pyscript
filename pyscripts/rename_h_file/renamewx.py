import wx


class frame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, parent=None, id=wx.ID_ANY, title=u"密麻麻命名机", pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(500, 300), wx.Size(500, 300))
        self.SetFont(wx.Font(11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑"))
        self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        self.m_menubar1 = wx.MenuBar(0)
        self.m_menubar1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        self.m_menu1 = wx.Menu()
        self.m_menubar1.Append(self.m_menu1, u"文件")

        self.m_menu2 = wx.Menu()
        self.m_menubar1.Append(self.m_menu2, u"操作")

        self.SetMenuBar(self.m_menubar1)

        msize = wx.BoxSizer(wx.VERTICAL)

        fsize = wx.BoxSizer(wx.HORIZONTAL)

        self.m_textCtrl1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TE_READONLY)
        self.m_textCtrl1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))
        self.m_textCtrl1.SetMinSize(wx.Size(400, -1))

        fsize.Add(self.m_textCtrl1, 0, wx.ALL, 5)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"选择目录", wx.DefaultPosition, wx.DefaultSize, 0)
        fsize.Add(self.m_button1, 0, wx.ALL, 5)

        msize.Add(fsize, 0, wx.TOP, 5)

        self.m_staticline1 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        msize.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5)

        self.m_button28 = wx.Button(self, wx.ID_ANY, u"开始批量重命名", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button28.SetFont(
            wx.Font(26, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑"))

        msize.Add(self.m_button28, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.SetSizer(msize)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


if __name__ == '__main__':
    app = wx.App()
    fra = frame()
    fra.Show()
    app.MainLoop()
