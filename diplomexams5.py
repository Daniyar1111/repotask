import tkinter as tk
from tkinter import messagebox


def calculate_sum():
    try:
        num = entry.get()
        if not num.isdigit():
            raise ValueError("Бүтін санды енгізіңіз")
        selected_loop = loop_var.get()

        if selected_loop == 1:  # Используем цикл for
            total = sum(int(digit) for digit in num if int(digit) % 3 == 0)
        else:  # Используем цикл while
            total = 0
            i = 0
            while i < len(num):
                digit = int(num[i])
                if digit % 3 == 0:
                    total += digit
                i += 1

        result_var.set(str(total))
    except ValueError as e:
        messagebox.showerror("Қате", str(e))


def clear():
    entry.delete(0, tk.END)
    result_var.set("")
    loop_var.set(1)  # Устанавливаем значение по умолчанию для Radiobutton


# Создаем основное окно
root = tk.Tk()
root.title("Radiobutton виджетімен жұмыс істеу")

# Организуем виджеты по примеру на картинке
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Добавляем радиокнопки для выбора цикла
tk.Label(frame, text="Циклды тандаңыз:").grid(row=0, column=0, columnspan=2, sticky=tk.W)
loop_var = tk.IntVar(value=1)
for_loop_radio = tk.Radiobutton(frame, text="for", variable=loop_var, value=1)
for_loop_radio.grid(row=1, column=0, sticky=tk.W)
while_loop_radio = tk.Radiobutton(frame, text="while", variable=loop_var, value=2)
while_loop_radio.grid(row=2, column=0, sticky=tk.W)

# Добавляем поле для ввода числа
tk.Label(frame, text="Бүтін сан енгізіңіз:").grid(row=3, column=0, columnspan=2, sticky=tk.W)
entry = tk.Entry(frame)
entry.grid(row=4, column=0, columnspan=2, sticky=tk.W + tk.E)

# Добавляем поле для вывода результата
(tk.Label(frame, text="3-ке қалдықсыз бөлінетін цифрларының қосындысы:")
 .grid(row=5, column=0, columnspan=2, sticky=tk.W))
result_var = tk.StringVar()
result_entry = tk.Entry(frame, textvariable=result_var, state="readonly")
result_entry.grid(row=6, column=0, columnspan=2, sticky=tk.W + tk.E)

# Добавляем кнопки "Орындау" и "Тазарту"
calculate_button = tk.Button(frame, text="Орындау", command=calculate_sum)
calculate_button.grid(row=7, column=0, pady=5)
clear_button = tk.Button(frame, text="Тазарту", command=clear)
clear_button.grid(row=7, column=1, pady=5)

root.mainloop()
