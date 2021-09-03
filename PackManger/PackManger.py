import tkinter

mwindow=tkinter.Tk()

mwindow.geometry("400x100+150+150")
mwindow.title("Welcome Tkinter")

mwindow.configure(background="blue")

button1=tkinter.Button(mwindow,text="Omar")
button1.pack(side="top")
button2=tkinter.Button(mwindow,text="Omar")
button2.pack(side="top")
button3=tkinter.Button(mwindow,text="Omar")
button3.pack(side="top")

mwindow.mainloop()