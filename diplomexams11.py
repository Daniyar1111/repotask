import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def sum_primes_for(n):
    prime_sum = 0
    for i in range(2, n + 1):
        if is_prime(i) and i != n:
            prime_sum += i
    return prime_sum


def sum_primes_while(n):
    prime_sum = 0
    i = 2
    while i < n:
        if is_prime(i):
            prime_sum += i
        i += 1
    return prime_sum


def calculate_primes():
    try:
        num = int(entry.get())
        if num < 3:
            raise ValueError("2-ден артық жай сан енгізіңіз")

        cycle_type = cycle_var.get()
        if cycle_type == "for":
            result = sum_primes_for(num)
        elif cycle_type == "while":
            result = sum_primes_while(num)
        else:
            raise ValueError("Циклдің түрін таңдаңыз")

        result_var.set(str(result))
    except ValueError as e:
        messagebox.showerror("Қате", str(e))


# Функция для очистки полей ввода
def clear_fields():
    entry.delete(0, tk.END)
    result_var.set("")
    cycle_var.set("")


# Создаем основное окно
root = tk.Tk()
root.title("Жай сандардың қосындысы")

# Создаем фрейм для виджетов
frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

# Создаем виджеты
tk.Label(frame, text="Циклдің түрін таңдаңыз:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
cycle_var = tk.StringVar()
cycle_combobox = Combobox(frame, textvariable=cycle_var, values=["for", "while"])
cycle_combobox.grid(row=1, column=0, padx=10, pady=5, sticky="w")

tk.Label(frame, text="Бүтін сан енгізіңіз:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry = tk.Entry(frame)
entry.grid(row=3, column=0, padx=10, pady=5, sticky="w")

tk.Label(frame, text="Cанға дейінгі жай сандардың қосындысы:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
result_var = tk.StringVar()
result_entry = tk.Entry(frame, textvariable=result_var, state="readonly")
result_entry.grid(row=5, column=0, padx=10, pady=5, sticky="w")

calculate_button = tk.Button(frame, text="Орындау", command=calculate_primes)
calculate_button.grid(row=6, column=0, padx=10, pady=5)

clear_button = tk.Button(frame, text="Тазарту", command=clear_fields)
clear_button.grid(row=6, column=1, padx=10, pady=5)

root.mainloop()
