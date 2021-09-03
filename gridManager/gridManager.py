#import tkinter
import tkinter

#create main window
main_window = tkinter.Tk()


#create 4 buttons
B1 = tkinter.Button(main_window,text = 'Button1')
B2 = tkinter.Button(main_window,text = 'Button2')
B3 = tkinter.Button(main_window,text = 'Button3')
B4 = tkinter.Button(main_window,text = 'Button4')

#display the buttons
B1.grid( row = 0, column = 1)
B2.grid( row = 1, column = 0)
B3.grid( row = 1, column = 2)
B4.grid( row = 2, column = 1)

#run the main window
main_window.mainloop()