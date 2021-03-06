import wx
import sqlite3 as lite
import sys

class dogs(wx.Frame):

        def __init__(self, parent,id):
                wx.Frame.__init__(self,parent,id,'Dog Grooming Database',size=(680,520))
                panel=wx.Panel(self)
                button=wx.Button(panel, label='exit', pos=(320,380),size=(50,30))
                self.Bind(wx.EVT_BUTTON, self.closebutton,button)
                self.Bind(wx.EVT_CLOSE, self.closewindow)

                status=self.CreateStatusBar()
                menubar=wx.MenuBar()
                firstmenu=wx.Menu()
                secondmenu=wx.Menu()
                newitem = firstmenu.Append(wx.NewId(),"New Entry","Adds New Entry for Dogs")
                exititem = firstmenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
                edititem = secondmenu.Append(wx.NewId(),"Edit Entry...","makes Nessasary Dog Entry")
                menubar.Append(firstmenu,"File")
                menubar.Append(secondmenu,"Edit")
                
                con = lite.connect('dog.DB')

                with con:
    
                    con.row_factory = lite.Row
       
                    cur = con.cursor() 
                    cur.execute("SELECT * FROM dog")

                    rows = cur.fetchall()

                    for row in rows:
                        dogsNumber = row["dogId"]
                        dogsName = row["dogname"]
                        dogsOwner = row["dogowner"]
                        print "%s %s %s" % (dogsNumber, dogsName, dogsOwner)

                
                self.SetMenuBar(menubar)
                self.Bind(wx.EVT_MENU, self.closebutton, exititem)
                self.Bind(wx.EVT_MENU, self.newobject, newitem)

                sexanswer = "default"
                nameanswer = "Default"

                wx.CheckBox(panel, -1, "pretty doggy", (80,80),(160,-1))
                wx.CheckBox(panel, -1, "ugly doggy", (80,100),(160,-1))
                wx.CheckBox(panel, -1, "Kill it with fire doggy", (80,120),(160,-1))

                mylist=['doggy 1', 'dodgey dog', 'shits eveerywhere dog', 'petable goggeh']
                print "%s %s %s" % (dogsNumber, dogsName, dogsOwner)
                cunt=wx.ListBox(panel, -1,(200,200),(-1,-1),mylist, wx.LB_SINGLE)
                cunt.SetSelection(2)
                
                custom=wx.StaticText(panel, -1,"Your dog is a: "+sexanswer+"\nYour dogs name is:"+nameanswer+"\nYour details are: \n"+"\n"+row["dogname"]+"\n"+row["dogowner"],(-1,-1), (260, -1))
##                custom.SetForegroundColour('pink')
##                custom.SetBackgroundColour('green')
##                sirslider=wx.Slider(panel, -1, 1,1,25, pos=(50,50), size=(450,-1), style=wx.SL_AUTOTICKS | wx.SL_LABELS)
##                sirslider.SetTickFreq(1,1)
##                myspinner=wx.SpinCtrl(panel, -1, "", (300, 300), (90,-1))
##                myspinner.SetRange(1,25)
##                myspinner.SetValue(1)

##                names=['Mark','Clare','Dave']
##                modal=wx.SingleChoiceDialog(None, "Whats ur name", "Im lost", names)
##                if modal.ShowModal()==wx.ID_OK:
##                        print "Your name is %s\n" % modal.GetStringSelection()
##                modal.Destroy()
                
        def closebutton(self, event):
                self.Close(True)

        def closewindow(self, event):
                self.Destroy()

        def newobject(self, event):
                sexchoice=wx.SingleChoiceDialog(None, 'Male or Bitch?', 'Sex?',['Male','bitch', 'Neutered'])
                if sexchoice.ShowModal()==wx.ID_OK:
                        sexvar=sexchoice.GetStringSelection()
                        
                namebox=wx.TextEntryDialog(None, 'Dogs name:','Dogs Details',"First name")
                if namebox.ShowModal()==wx.ID_OK:

                        namevar=namebox.GetValue()
                
                agechoice=wx.TextEntryDialog(None, 'Dogs Age:', 'Dogs Details','Dogs age.')
                if agechoice.ShowModal()==wx.ID_OK:
                
                        agevar=agechoice.GetValue()
                        
                breedname=wx.SingleChoiceDialog(None,'What kind of dog is it?','Breed', ['Collie', 'Wire hair Terrier', 'smooth hair Terrier', 'Husky', 'Bichon', 'Long Hair Spaniel', 'Short haired spaniel', 'Malamute', 'Akita', 'Bulldog', 'Mastiff', 'PitBull', 'st. bernard', 'shih tzuz'])
                if breedname.ShowModal()==wx.ID_OK:
                
                        breedvar=breedname.GetStringSelection()
                
                ownerentry=wx.TextEntryDialog(None, 'Owners Name: ','Owners Details', 'Dogs Owners name.' )
                if ownerentry.ShowModal()==wx.ID_OK:
                        
                        ownervar=ownerentry.GetValue()
                        
                mobileentry=wx.TextEntryDialog(None, 'Owners Mobile', 'Owners Mobile', 'Owners mobile')
                if mobileentry.ShowModal()==wx.ID_OK:
                        mobvar=mobileentry.GetValue()
               
                altnoentry=wx.TextEntryDialog(None, 'Secondary Number','Backup Number','Alt Number' )
                if altnoentry.ShowModal()==wx.ID_OK:
                        altvar=altnoentry.GetValue()
                        
                        con = lite.connect('dog.DB')

                        with con:
                                cur = con.cursor() 
                                cur.execute("INSERT INTO dog (dogname, dogage, dogbreed, dogcreated, dogowner, dogmobile, dogaltcontact, dogsex) VALUES (?, ?, ?, datetime('now'), ?, ?, ?, ?)", (namevar, agevar, breedvar, ownervar, mobvar, altvar, sexvar))


if __name__=='__main__':
        app=wx.App(False)
        frame=dogs(parent=None,id=-1)
        frame.Show()
        app.MainLoop()

        
