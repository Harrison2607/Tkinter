from tkinter import*
from tkinter import messagebox
root=Tk()
root.geometry('200x200')
def msg():
    messagebox.showwarning("Alert","Stop!there is a virus")
btn=Button(root,text="Scan for virus",command=msg)
btn.pack()
def yo():
    a=messagebox.askyesno("just a sec i am having a call")
    if a :
        print("User selected yes")
    else:
        print("User selected no")
btn2=Button(root,text="ask yes or no",command=yo)
btn2.pack()
def info():
    b=messagebox.showinfo("Information","This is just an information message")
btn3=Button(text="Information",command=info)
btn3.pack()

    
root.mainloop()
