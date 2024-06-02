import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def calculate_factorial():
    try:
        num_str = entry_number.get()
        if not num_str.isdigit():
            raise ValueError("Бүтін санды енгізіңіз")

        selected_cycle = cycle_combobox.get()

        if selected_cycle == "for":
            fact = factorial_for_cycle(num_str)
        elif selected_cycle == "while":
            fact = factorial_while_cycle(num_str)
        else:
            raise ValueError("Циклдің түрін таңдаңыз")

        result_label.config(text=f"Енгізілген санның факториалы: {fact}")
    except ValueError as e:
        messagebox.showerror("Қате", str(e))


def factorial_for_cycle(num_str):
    num = int(num_str)
    if num < 0:
        return "Қате"
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact


def factorial_while_cycle(num_str):
    num = int(num_str)
    if num < 0:
        return "Қате"
    fact = 1
    i = 1
    while i <= num:
       fact *= i
       i += 1
    return fact


def clear_fields():
    entry_number.delete(0, tk.END)
    cycle_combobox.set("")
    result_label.config(text="")


# Создание главного окна
root = tk.Tk()
root.title("Combobox факториал")

# Метка и Combobox для выбора цикла
label_cycle = tk.Label(root, text="Циклді таңдаңыз:")
label_cycle.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

cycle_combobox = ttk.Combobox(root, values=["for", "while"])
cycle_combobox.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

# Ввод числа
label_number = tk.Label(root, text="Бүтін санды енгізіңіз:")
label_number.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

entry_number = tk.Entry(root)
entry_number.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

# Кнопка для вычисления произведения цифр
calculate_button = tk.Button(root, text="Орындау", command=calculate_factorial)
calculate_button.grid(row=3, column=0, padx=10, pady=5)

# Кнопка для очистки полей
clear_button = tk.Button(root, text="Тазарту", command=clear_fields)
clear_button.grid(row=3, column=1, padx=10, pady=5)

# Отображение результата
result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Запуск главного цикла обработки событий
root.mainloop()
