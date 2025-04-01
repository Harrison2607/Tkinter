import tkinter as tk
from tkinter import messagebox
def calculate_denominations():
    try:
       amount = int(entry_amount.get())
       if amount <= 0:
          messagebox.showerror("Error", "Please enter a positive amount")
          return
       denominations = [500, 200, 100, 50, 20, 10, 5, 2, 1]
       result = ""
       for i in denominations:
           count = amount // i
           if count > 0:
              result += f"{i} = {count}\n"
              amount %= i
       tk.Label_result.config(text=result)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")
window=tk.Tk()
window.title("Denomination calculator")
window.geometry("300x400")
tk.Label(window,text="Enter your amount",font=("Arial",12)).pack(pady=10)
entry_amount=tk.Entry(window,font=("Arial",12))
entry_amount.pack(pady=5)
tk.Button(window,text="Calculate",command=calculate_denominations,font=("Arial",12),bg="blue",fg="white").pack()
tk.Label_result=tk.Label(window,text="",font=("Arial",12))
tk.Label_result.pack(pady=10)
window.mainloop()