import tkinter

mwindow=tkinter.Tk()

mwindow.geometry("400x100+150+150")
mwindow.title("Welcome Tkinter")

mwindow.configure(background="blue")

button1=tkinter.Button(mwindow,text="Omar")
button1.place(x="5m",y="5m")
button2=tkinter.Button(mwindow,text="Omar")
button2.place(x="10m",y="10m")
button3=tkinter.Button(mwindow,text="Omar")
button3.place(x="15m",y="15m")

mwindow.mainloop()