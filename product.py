import tkinter as tk
def fp():
    num1=int(entry1.get())
    num2=int(entry2.get())
    result=num1*num2
    result_label.config(text=f"Product: {result}")
window=tk.Tk()
window.title('Product Finder')
window.geometry('300x400')
entry1=tk.Entry(window)
entry2=tk.Entry(window)
btn=tk.Button(window,text='Find Product',command=fp)
result_label=tk.Label(window,text='The product is:')
entry1.pack()
entry2.pack()
btn.pack()
result_label.pack()
window.mainloop()