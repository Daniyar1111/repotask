import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def calculate_product():
    try:
        num_str = entry_number.get()
        if not num_str.isdigit():
            raise ValueError("Бүтін санды енгізіңіз")

        selected_cycle = cycle_combobox.get()

        if selected_cycle == "for":
            product = product_for_cycle(num_str)
        elif selected_cycle == "while":
            product = product_while_cycle(num_str)
        else:
            raise ValueError("Циклдің түрін таңдаңыз")

        result_label.config(text=f"Сандардың көбейтіндісі: {product}")
    except ValueError as e:
        messagebox.showerror("Қате", str(e))


def product_for_cycle(num_str):
    product = 1
    for digit in num_str:
        if digit != '0':
            product *= int(digit)
    return product


def product_while_cycle(num_str):
    num = int(num_str)
    product = 1
    while num > 0:
        digit = num % 10
        if digit != 0:
            product *= digit
        num = num // 10
    return product


def clear_fields():
    entry_number.delete(0, tk.END)
    cycle_combobox.set("")
    result_label.config(text="")


# Создание главного окна
root = tk.Tk()
root.title("Сандардың көбейтіндісі")

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
calculate_button = tk.Button(root, text="Орындау", command=calculate_product)
calculate_button.grid(row=3, column=0, padx=10, pady=5)

# Кнопка для очистки полей
clear_button = tk.Button(root, text="Тазарту", command=clear_fields)
clear_button.grid(row=3, column=1, padx=10, pady=5)

# Отображение результата
result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Запуск главного цикла обработки событий
root.mainloop()
