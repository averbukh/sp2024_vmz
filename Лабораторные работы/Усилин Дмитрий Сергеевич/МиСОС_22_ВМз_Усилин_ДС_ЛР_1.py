import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def func(a1, b1, a2, b2, a3, b3, x):
    return a1 * math.sin(b1 * x) + a2 * math.sin(b2 * x) + a3 * math.sin(b3 * x)

def main():
    # Ввод данных пользователя
    a1 = float(input("Введите a1: "))
    b1 = float(input("Введите b1: "))
    a2 = float(input("Введите a2: "))
    b2 = float(input("Введите b2: "))
    a3 = float(input("Введите a3: "))
    b3 = float(input("Введите b3: "))
    x0 = float(input("Введите начальное значение x: "))
    xk = float(input("Введите конечное значение x: "))
    delta_x = float(input("Введите шаг: "))

    # Генерация векторов x и y
    x_values = []
    y_values = []

    x = x0
    while x <= xk:
        y = func(a1, b1, a2, b2, a3, b3, x)
        x_values.append(x)
        y_values.append(y)
        x += delta_x

    # Отображение векторов в виде таблицы
    print(f"{'x':<10}{'y':<10}")
    for x, y in zip(x_values, y_values):
        print(f"{x:<10.2f}{y:<10.2f}")

    # Построение графика
    plt.plot(x_values, y_values, label='y(x)', color='b')
    plt.title('y(x) = a1 * sin(b1 * x) + a2 * sin(b2 * x) + a3 * sin(b3 * x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.grid()
    plt.legend()

    # Сохраняем график в файл
    plt.savefig('graph.png')

if __name__ == "__main__":
    main()
