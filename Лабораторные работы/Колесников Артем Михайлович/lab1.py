import numpy as np
import matplotlib.pyplot as plt

# Функция для расчета y(x)
def y(x, a1, b1, a2, b2, a3, b3):
    return a1 * np.sin(b1 * x) + a2 * np.sin(b2 * x) + a3 * np.sin(b3 * x)

# Ввод данных от пользователя
a1 = float(input("Введите a1: "))
b1 = float(input("Введите b1: "))
a2 = float(input("Введите a2: "))
b2 = float(input("Введите b2: "))
a3 = float(input("Введите a3: "))
b3 = float(input("Введите b3: "))
x0 = float(input("Введите начальное значение x0: "))
xk = float(input("Введите конечное значение xк: "))
delta_x = float(input("Введите шаг Δx: "))

# Генерация массива x
x_values = np.arange(x0, xk + delta_x, delta_x)

# Расчет y для каждого x
y_values = y(x_values, a1, b1, a2, b2, a3, b3)

# Отображение векторов x и y в виде таблицы
print("\nТаблица значений x и y:")
print("{:<10} {:<10}".format("x", "y"))
for x, y_val in zip(x_values, y_values):
    print("{:<10} {:<10.5f}".format(x, y_val))

# Построение графика y(x)
plt.figure(figsize=(10, 5))
plt.plot(x_values, y_values, label='y(x)', color='blue')
plt.title('График функции y(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.legend()
plt.show()