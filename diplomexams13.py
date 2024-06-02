import tkinter as tk
from tkinter import messagebox


def calculate_resistance():
    try:
        length = float(entry_length.get())
        width = float(entry_width.get())
        height = float(entry_height.get())

        if length <= 0 or width <= 0 or height <= 0:
            raise ValueError("Оң сандар жазылу керек")

        area = 2 * (length + width) * height
        result_var.set(f"{area:.2f}")
    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))


def clear_fields():
    entry_length.delete(0, tk.END)
    entry_width.delete(0, tk.END)
    entry_height.delete(0, tk.END)
    result_var.set("")


# Создаем основное окно
root = tk.Tk()
root.title("Параллелепипед бетінің ауданы")

# Создаем фрейм для виджетов
frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

# Создаем виджеты
header_label = tk.Label(frame, text="Бастапқы мәліметтерді енгізіңіз:")
header_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="we")

tk.Label(frame, text="Ұзындығы (см) ->").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_length = tk.Entry(frame)
entry_length.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame, text="Ені (см) ->").grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_width = tk.Entry(frame)
entry_width.grid(row=2, column=1, padx=10, pady=5,)

tk.Label(frame, text="Биіктігі (см) ->").grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_height = tk.Entry(frame)
entry_height.grid(row=3, column=1, padx=10, pady=5,)

tk.Label(frame, text="Бетінің ауданы (см. кв.) ->").grid(row=4, column=0, padx=10, pady=5, sticky="w")
result_var = tk.StringVar()
result_entry = tk.Entry(frame, textvariable=result_var, state="readonly")
result_entry.grid(row=4, column=1, padx=10, pady=5,)

calculate_button = tk.Button(frame, text="Орындау", command=calculate_resistance)
calculate_button.grid(row=5, column=0, padx=10, pady=5,)

clear_button = tk.Button(frame, text="Тазарту", command=clear_fields)
clear_button.grid(row=5, column=1, padx=10, pady=5,)

root.mainloop()
