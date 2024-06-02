import tkinter as tk
from tkinter import messagebox


def show_text():
    input_text = entry_text.get()
    result_label.config(text=input_text)
    if input_text == "":
        messagebox.showinfo('Қате', 'Мәтінді енгізіңіз')
    return


def clear_fields():
    entry_text.delete(0, tk.END)
    result_label.config(text="")


root = tk.Tk()
root.title("Мәтін енгізу")

frame = tk.Frame(root, padx=15, pady=15)
frame.pack()

label = tk.Label(frame, text="Мәтінді енгізіңіз ->")
label.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="w")

entry_text = tk.Entry(frame)
entry_text.grid(row=0, column=2, padx=10, pady=5, sticky="e")

do_button = tk.Button(frame, text="Орындау", command=show_text)
do_button.grid(row=1, column=0, padx=10, pady=5, sticky="w")

clear_button = tk.Button(frame, text="Тазарту", command=clear_fields)
clear_button.grid(row=1, column=2, padx=10, pady=5, sticky="w")

result_label = tk.Label(frame, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="w")

root.mainloop()
