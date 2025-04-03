import tkinter as tk
window=tk.Tk()
window.geometry('400x400')
window.title("Restraunt management")
menu=["Pizza","Burger","Popcorn","Mango Shake"]
price={"Pizza":8.99,"Burger":3.00,"Popcorn":5.49,"Mango Shake":4.49}
quantity=[]
def calculate_total():
    total=0
    for item,var in zip(menu,quantity):
        total+=price[item]*int(var.get())
    total_var.set(f"Total:${total:.2f}")

for i in menu:
    frame=tk.Frame(window)
    frame.pack(pady=5)
    tk.Label(frame,text=f"{i}-${price[i]:.2f}").pack(side=tk.LEFT)
    var = tk.StringVar(value="0")
    quantity.append(var)
    tk.Entry(frame, textvariable=var, width=5).pack(side=tk.RIGHT)
total_var = tk.StringVar(value="Total: $0.00")
total_label = tk.Label(window, textvariable=total_var, font=("Arial", 12, "bold"))
total_label.pack(pady=10)
# Buttons
tk.Button(window, text="Calculate Total", command=calculate_total).pack(pady=5)
window.mainloop()
