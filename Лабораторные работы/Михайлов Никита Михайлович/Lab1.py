import numpy as np
import matplotlib.pyplot as plt

def calculate_and_plot(a1, b1, a2, b2, a3, b3, x0, xk, dx):
    # Создание вектора x
    x = np.arange(x0, xk + dx, dx)
    # Расчет значений функции y(x)
    y = a1 * np.sin(b1 * x) + a2 * np.sin(b2 * x) + a3 * np.sin(b3 * x)
    
    # Вывод таблицы значений
    print(" x   |   y ")
    for xi, yi in zip(x, y):
        print(f"{xi:.3f} | {yi:.3f}")
    
    # Построение графика
    plt.plot(x, y, marker='o', linestyle='-', color='g', label='y(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График функции y(x)')
    plt.legend()
    plt.grid()
    
    # Сохранение графика в файл SVG
    plt.savefig("plot.svg", format="svg")
    
    plt.show()
    
# Ввод данных от пользователя
a1 = float(input("Введите a1: "))
b1 = float(input("Введите b1: "))
a2 = float(input("Введите a2: "))
b2 = float(input("Введите b2: "))
a3 = float(input("Введите a3: "))
b3 = float(input("Введите b3: "))
x0 = float(input("Введите начальное значение x0: "))
xk = float(input("Введите конечное значение xk: "))
dx = float(input("Введите шаг dx: "))

calculate_and_plot(a1, b1, a2, b2, a3, b3, x0, xk, dx)