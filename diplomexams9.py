import tkinter as tk
from tkinter import messagebox


def calculate_resistance():
    try:
        r1 = float(entry_r1.get())
        r2 = float(entry_r2.get())

        if r1 <= 0 or r2 <= 0:
            raise ValueError("Оң сандар жазылу керек")

        total_resistance = (r1 * r2) / (r1 + r2)
        result_var.set(f"{total_resistance:.2f}")
    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))


def clear_fields():
    entry_r1.delete(0, tk.END)
    entry_r2.delete(0, tk.END)
    result_var.set("")


# Создаем основное окно
root = tk.Tk()
root.title("Параллель кедергіні есептеу")

# Создаем фрейм для виджетов
frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

# Создаем виджеты
header_label = tk.Label(frame, text="Бастапқы мәліметтерді енгізіңіз:")
header_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="we")

tk.Label(frame, text="Бірінші кедергінің шамасы (Ом) ->").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_r1 = tk.Entry(frame)
entry_r1.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame, text="Екінші кедергінің шамасы (Ом) ->").grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_r2 = tk.Entry(frame)
entry_r2.grid(row=2, column=1, padx=10, pady=5,)

tk.Label(frame, text="Тізбектің кедергісі (Ом) ->").grid(row=4, column=0, padx=10, pady=5, sticky="w")
result_var = tk.StringVar()
result_entry = tk.Entry(frame, textvariable=result_var, state="readonly")
result_entry.grid(row=4, column=1, padx=10, pady=5,)

calculate_button = tk.Button(frame, text="Орындау", command=calculate_resistance)
calculate_button.grid(row=5, column=0, padx=10, pady=5,)

clear_button = tk.Button(frame, text="Тазарту", command=clear_fields)
clear_button.grid(row=5, column=1, padx=10, pady=5,)

root.mainloop()
