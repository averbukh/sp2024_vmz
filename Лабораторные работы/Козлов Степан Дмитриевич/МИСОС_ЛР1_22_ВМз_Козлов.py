import numpy as np
import matplotlib.pyplot as plt

def calculate_y(a1, b1, a2, b2, a3, b3, x):
    """Вычисляет значение y(x) для заданного x."""
    return a1 * np.sin(b1 * x) + a2 * np.sin(b2 * x) + a3 * np.sin(b3 * x)

def main():
    # Запрос значений у пользователя
    params = input("Введите значения a1, b1, a2, b2, a3, b3 (через пробел): ")
    a1, b1, a2, b2, a3, b3 = map(float, params.split(' '))

    x0 = float(input("Введите начальное значение x0: "))
    xk = float(input("Введите конечное значение xk: "))
    delta_x = float(input("Введите шаг Δx: "))

    # Генерация массива x и вычисление y
    x_values = np.arange(x0, xk, delta_x)
    y_values = calculate_y(a1, b1, a2, b2, a3, b3, x_values)

    # Вывод в виде таблицы
    print("\nТаблица значений:")
    print(" x         |    y")
    print("--------------------")
    for x, y in zip(x_values, y_values):
        print(f"{x:8.2f} | {y:8.2f}")

    # Построение графика
    plt.figure(figsize=(10, 5))
    plt.plot(x_values, y_values, label='y(x)', color='blue')
    plt.title('График функции y(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.legend()

    # Сохранение графика
    plt.savefig('МИСОС_ЛР1_22_ВМз_Козлов.png')
    plt.show()

if __name__ == "__main__":
    main()