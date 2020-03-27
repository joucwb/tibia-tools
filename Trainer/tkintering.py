from tkinter import *

root = Tk()
root.title('Calculator')

e = Entry(root, width=50, fg="blue", borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
e.pack()
e.insert(0, 'Enter your name: ') 

def myClick():
	myLabel = Label(root, text=e.get())
	myLabel.pack()

myButton = Button(root, text='LIKE ME!', command=myClick)

root.mainloop()

