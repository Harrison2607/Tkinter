from tkinter import*
root=Tk()
root.geometry('200x200')
def bcl():
    print("This is code")
btn=Button(root,text="Click me",command=bcl)
btn.pack()
root.mainloop()