import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Ввод значений
a1 = float(input("Введите значение a1: "))
b1 = float(input("Введите значение b1: "))
a2 = float(input("Введите значение a2: "))
b2 = float(input("Введите значение b2: "))
a3 = float(input("Введите значение a3: "))
b3 = float(input("Введите значение b3: "))
x0 = float(input("Введите начальное значение x (x0): "))
xk = float(input("Введите конечное значение x (xk): "))
dx = float(input("Введите шаг Δx: "))

# Создание вектора x
x_values = np.arange(x0, xk + dx, dx)

# Расчет значений функции y(x)
y_values = a1 * np.sin(b1 * x_values) + a2 * np.sin(b2 * x_values) + a3 * np.sin(b3 * x_values)

# Отображение таблицы значений x и y
data = {'x': x_values, 'y': y_values}
df = pd.DataFrame(data)
print(df)

# Построение графика
plt.plot(x_values, y_values, label='y(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции y(x)')
plt.legend()

# Сохранение графика в формате SVG
plt.savefig('graph.svg', format='svg')

# Показать график
plt.show()
