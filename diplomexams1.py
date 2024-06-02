import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def calculate_sum():
    num_str = entry_number.get()
    if not num_str.isdigit():
        messagebox.showerror("Қате", "Бүтін санды енгізіңіз")
        return

    num = int(num_str)
    selected_cycle = cycle_combobox.get()

    if selected_cycle == "for":
        sum_digits = sum_for_cycle(num)
    elif selected_cycle == "while":
        sum_digits = sum_while_cycle(num)
    else:
        messagebox.showerror("Қате", "Циклдің түрін таңдаңыз")
        return

    result_label.config(text=f"Цифрлардың қосындысы: {sum_digits}")


def sum_for_cycle(num):
    sum_digits = 0
    for digit in str(num):
        sum_digits += int(digit)
    return sum_digits


def sum_while_cycle(num):
    sum_digits = 0
    while num > 0:
        sum_digits += num % 10
        num = num // 10
    return sum_digits


def clear_fields():
    entry_number.delete(0, tk.END)
    cycle_combobox.set("")
    result_label.config(text="")


# Создание главного окна
root = tk.Tk()
root.title("Combobox виджетімен жұмыс істеу")

# Метка и Combobox для выбора цикла
label_cycle = tk.Label(root, text="Циклды таңдаңыз:")
label_cycle.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

cycle_combobox = ttk.Combobox(root, values=["for", "while"])
cycle_combobox.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

# Ввод числа
label_number = tk.Label(root, text="Санның цифрларының қосындысы:")
label_number.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

entry_number = tk.Entry(root)
entry_number.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

# Кнопка для вычисления суммы цифр
calculate_button = tk.Button(root, text="Орындау", command=calculate_sum)
calculate_button.grid(row=3, column=0, padx=10, pady=5)

# Кнопка для очистки полей
clear_button = tk.Button(root, text="Тазарту", command=clear_fields)
clear_button.grid(row=3, column=1, padx=10, pady=5)

# Отображение результата
result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Запуск главного цикла обработки событий
root.mainloop()
