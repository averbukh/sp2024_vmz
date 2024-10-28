import numpy as np
import matplotlib.pyplot as plt

# Ввод параметров
a1 = float(input("Введите a1: "))
b1 = float(input("Введите b1: "))
a2 = float(input("Введите a2: "))
b2 = float(input("Введите b2: "))
a3 = float(input("Введите a3: "))
b3 = float(input("Введите b3: "))
x0 = float(input("Введите начальное значение x (x0): "))
xk = float(input("Введите конечное значение x (xk): "))
dx = float(input("Введите шаг Δx: "))

# Создание массива значений x от x0 до xk с шагом dx
x_values = np.arange(x0, xk + dx, dx)

# Функция y(x)
def y_function(x):
    return a1 * np.sin(b1 * x) + a2 * np.sin(b2 * x) + a3 * np.sin(b3 * x)

# Вычисление значений y
y_values = y_function(x_values)

# Вывод таблицы значений
print("Таблица значений:")
print("x\t\ty")
for x, y in zip(x_values, y_values):
    print(f"{x:.5f}\t{y:.5f}")

# Построение графика
plt.plot(x_values, y_values, label='y(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции y(x)')
plt.legend()

# Сохранение графика
file_format = input("Введите формат для сохранения (BMP или SVG): ").strip().lower()

if file_format == 'bmp':
    plt.savefig('graph.bmp', format='bmp')
    print("График сохранен в формате BMP")
elif file_format == 'svg':
    plt.savefig('graph.svg', format='svg')
    print("График сохранен в формате SVG")
else:
    print("Неправильный формат. График сохранен в формате PNG по умолчанию.")
    plt.savefig('graph.png', format='png')

plt.show()
