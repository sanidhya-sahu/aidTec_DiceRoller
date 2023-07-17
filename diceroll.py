import random
import time
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font

root = Tk()
root.iconbitmap("dice.ico")
root.geometry("1000x700")
root.title("Dice Roller")
root.resizable(False,True)
widget_references = []  # List to store references to created widgets

def start():
    # Remove previously created widgets
    for widget in widget_references:
        widget.destroy()

    if a.get() != "q":
        try:
            n = int(a.get())
            roll_dice(n)
        except ValueError:
            messagebox.showerror("Error", "Enter a valid number")
    else:
        choice = messagebox.askyesno("Exit ?", "Do you want leave Dice Roller")
        if choice:
            root.destroy()


def roll_dice(number):
    a.config(state="disabled")
    but.config(state="disabled")
    for i in range(number):
        lab = Text(root, height=1, width=20,font=fontt)
        lab.insert(END, f"Rolling dice {i + 1} ...\n")
        lab.configure(state='disabled')
        widget_references.append(lab)  # Add lab widget reference to the list
        lab.grid(row=i + 3, column=1, pady=5)
        indicator = Label(root, text='''🎲''',font=(20))
        indicator.grid(row=i + 3, column=3, pady=5)
        root.update()
        time.sleep(1)  # Wait for 1 seconds
        value = random.randint(1, 6)
        indicator.grid_forget()
        root.update()
        # print(value)
        result = Text(root, height=1, width=5,font=fontt)
        result.insert(END, str(value))
        result.configure(state='disabled')
        widget_references.append(result)  # Add result widget reference to the list
        result.grid(row=i + 3, column=2, pady=5)
        root.update()
    a.config(state="enabled")
    but.config(state="enabled")


bold_font = font.Font(weight="bold",size=40)
detail_font = font.Font(weight="bold",size=15)
fontt=font.Font(size=12)
ghost = Label(root,width=30)
ghost.grid(row=0, column=0, pady=10)
mainhead = Label(root, text='''Dice Roller''',font=bold_font,fg="black")
mainhead.grid(row=0, column=1, columnspan=3, pady=10)
head = Label(root, text='''▪️Enter number of dices to be roll or enter "q" to quit rolling
▪️Do not enter more than 15 number''',fg="grey",font=detail_font)
head.grid(row=1, column=1, columnspan=2, pady=10)
a = ttk.Entry(root, width=20,font=fontt,justify="center")
a.grid(row=2, column=1, pady=5)
but = ttk.Button(root, text="Roll", command=start)
but.grid(row=2, column=2, pady=5)
root.mainloop()
