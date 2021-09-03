#import Data
import tkinter

def Enter_CB() :
	user = User_Entry.get()
	user = user.lower()
	
	Pass = Pass_Entry.get()
	
	if (user=="omar") and (Pass=="1234"):
		print("Correct")
	else:
		print("Incorrect")

rownum=3
colnum=3

def MainwindowInit():
	global mainW
	mainW = tkinter.Tk()
	mainW.geometry("210x150+500+200")
	mainW.title("Login")
	mainW.resizable(width=False,height=False)
	
	i=0
	while i < rownum :
		mainW.grid_rowconfigure(i,minsize=40)
		i+=1
		
	i=0
	while i < colnum :
		mainW.grid_columnconfigure(i,minsize=40)
		i+=1
		
	#mainW.configure(background="blue")

def LabelInit() :
	User_Label=tkinter.Label(mainW, text="user")
	Pass_Label=tkinter.Label(mainW, text="pass")
	User_Label.grid(row=0,column=0)
	Pass_Label.grid(row=1,column=0)
	
def EntryInit() :
	global User_Entry
	global Pass_Entry
	User_Entry=tkinter.Entry(mainW)
	Pass_Entry=tkinter.Entry(mainW,show="*")
	User_Entry.grid(row=0,column=1)
	Pass_Entry.grid(row=1,column=1)
	
def ButtonInit() :
	Enter_Button = tkinter.Button(mainW,text="Enter",command=Enter_CB)
	Enter_Button.grid(row=2,column=2)

