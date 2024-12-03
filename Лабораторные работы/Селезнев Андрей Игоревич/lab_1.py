import numpy as np
import matplotlib.pyplot as plt

# Получаем параметры от пользователя
coefficients = []
for i in range(1, 4):
    a = float(input(f"Введите коэффициент a{i}: "))
    b = float(input(f"Введите коэффициент b{i}: "))
    coefficients.append((a, b))

x_start = float(input("Введите начальное значение x: "))
x_end = float(input("Введите конечное значение x: "))
step = float(input("Введите шаг Δx: "))

# Формируем массив значений x
x_values = np.arange(x_start, x_end + step, step)

# Вычисляем значения функции y(x)
y_values = sum(a * np.sin(b * x_values) for a, b in coefficients)

# Выводим таблицу значений
print("\nТаблица значений x и y:")
print(f"{'x':>10} {'y':>10}")
for x, y in zip(x_values, y_values):
    print(f"{x:>10.4f} {y:>10.4f}")

# Строим график функции
plt.figure(figsize=(8, 5))
plt.plot(x_values, y_values, label='y(x)', color='blue', linewidth=2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции y(x)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()
