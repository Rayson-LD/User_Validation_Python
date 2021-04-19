import re
import wx
import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty('rate')                         
engine.setProperty('rate', 150)
class MyFrame(wx.Frame) :
    def __init__(self) :  
        wx.Frame.__init__(self,None,pos=wx.DefaultPosition, size=wx.Size(500,500),style=wx.MAXIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.MINIMIZE_BOX| wx.CLOSE_BOX | wx.CLIP_CHILDREN,title="Password Validation")
        panel= wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl1=wx.StaticText(panel,label="Enter Your Name :",size = wx.Size(400,30))
        lbl=wx.StaticText(panel,label="Enter Your Password :",size = wx.Size(400,30))
        note=wx.StaticText(panel,label="Note :Enter the valid Password ",size = wx.Size(400,70))
        self.txt1 = wx.TextCtrl(panel,style= wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt = wx.TextCtrl(panel,style= wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt1.SetFocus()
        self.txt.SetFocus()
        self.txt1.SetHint("Enter Your Name")
        self.txt.SetHint("Enter Your Password")
        self.btn = wx.ToggleButton(panel,-1,"Submit") 
        self.btn.Bind(wx.EVT_TOGGLEBUTTON,self.OnEnter)
        my_sizer.Add(lbl1, 0,wx.ALL,5)
        my_sizer.Add(self.txt1,0,wx.ALL,5)
        my_sizer.Add(lbl, 0,wx.ALL,5)
        my_sizer.Add(self.txt,0,wx.ALL,5)
        my_sizer.Add(note,0,wx.ALL,5)
        my_sizer.Add(self.btn,0,wx.ALIGN_CENTER)
        panel.SetSizer(my_sizer)
        self.Show()
    def OnEnter(self, event) :
        input1= self.txt1.GetValue()
        input = self.txt.GetValue()
        if input1=="" or input=="" :
            print("Please Enter your name or password")
            engine.say("Please Enter your name or password")
            engine.runAndWait()
        elif (len(input)<6 or len(input)<12) and re.search("[a-z]",input) and re.search("[0-9]",input) and re.search("[A-Z]",input) and re.search("[$#@]",input) :
            print("Welcome To Home "+input1)
            engine.say("Welcome To Home "+ input1)
            engine.runAndWait()
        else :
            print("Password is not Valid")
            engine.say("Password is not Valid")
            engine.runAndWait()     
if  __name__ == "__main__" :
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()    
