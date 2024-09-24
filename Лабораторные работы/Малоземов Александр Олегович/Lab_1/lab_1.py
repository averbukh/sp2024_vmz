import numpy as np
import matplotlib.pyplot as plt

# Запрашиваем ввод параметров у пользователя
a1 = float(input("Введите a1: "))
b1 = float(input("Введите b1: "))
a2 = float(input("Введите a2: "))
b2 = float(input("Введите b2: "))
a3 = float(input("Введите a3: "))
b3 = float(input("Введите b3: "))
x0 = float(input("Введите начальное значение x (x0): "))
xk = float(input("Введите конечное значение x (xк): "))
dx = float(input("Введите шаг Δx: "))

# Создаем массив значений x с шагом dx
x_values = np.arange(x0, xk + dx, dx)

# Вычисляем значения y(x)
y_values = a1 * np.sin(b1 * x_values) + a2 * np.sin(b2 * x_values) + a3 * np.sin(b3 * x_values)

# Отображаем таблицу значений x и y
print("\nТаблица значений x и y:")
print(f"{'x':>10} {'y':>10}")
for x, y in zip(x_values, y_values):
    print(f"{x:>10.4f} {y:>10.4f}")

# Строим график
plt.plot(x_values, y_values, label='y(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('График y(x)')
plt.grid(True)
plt.legend()
plt.show()
