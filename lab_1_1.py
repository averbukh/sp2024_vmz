import numpy as np
import matplotlib.pyplot as plt

# Задаем параметры
a1 = float(input("Введите a1: "))
b1 = float(input("Введите b1: "))
a2 = float(input("Введите a2: "))
b2 = float(input("Введите b2: "))
a3 = float(input("Введите a3: "))
b3 = float(input("Введите b3: "))
x0 = float(input("Введите начальное значение x0: "))
xk = float(input("Введите конечное значение xk: "))
delta_x = float(input("Введите шаг Δx: "))

# Создаем массив значений x
x_values = np.arange(x0, xk + delta_x, delta_x)
# Вычисляем значения y
y_values = a1 * np.sin(b1 * x_values) + a2 * np.sin(b2 * x_values) + a3 * np.sin(b3 * x_values)

# Выводим значения x и y
print("x\t\t y")
for x, y in zip(x_values, y_values):
    print(f"{x:.2f}\t {y:.2f}")