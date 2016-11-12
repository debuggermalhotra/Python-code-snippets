import wx

#application object
app=wx.App()

#creating a wx.Frame object.
frame=wx.Frame(None,-1,'simple.py')

frame.Show()

#enter the mainloop. The mainloop is an endless cycle.
app.MainLoop()
