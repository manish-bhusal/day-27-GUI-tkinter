import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text="I Am A Label", font=("Arial", 24))
my_label["text"] = "A new text"
my_label.grid(row=0, column=0)


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)

# Entry
input = tkinter.Entry(width=15)
# print(input.get())
input.grid(row=2, column=3)

# New Button


def button_click():
    print("Clicked")


button2 = tkinter.Button(text="NewButton", command=button_click)
button2.grid(row=0, column=2)

window.mainloop()
