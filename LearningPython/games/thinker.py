import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.geometry("640x480")
button = tkinter.Button(window, text="Click on me")
button.pack()

label = ttk.Label(window, text="LABELELLELELEL")
label.pack()

label.config(text="Hello World")
checkbox = ttk.Checkbutton(window, text="Free?")
checkbox.pack()

entry = ttk.Entry(window, width=20)
entry.pack()
entry.insert(0, "Becca")
entry.config(show="*")

week_day = tkinter.StringVar()
week_cb = ttk.Combobox(window, textvariable=week_day)
week_cb.pack()
week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
week_cb.config(values=week_days)

day = tkinter.StringVar()
ttk.Spinbox(window, from_=1, to=30, textvariable=day).pack()

notebook = ttk.Notebook(window)
notebook.pack()
first_frame = ttk.Frame()
second_frame = ttk.Frame()
notebook.add(first_frame, text="first frame")
notebook.add(second_frame, text="second frame")
tkinter.Button(first_frame, text="Click on me").pack()

tkinter.mainloop()
