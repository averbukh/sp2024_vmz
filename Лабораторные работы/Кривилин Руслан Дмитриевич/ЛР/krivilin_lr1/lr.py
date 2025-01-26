import numpy as np
import matplotlib.pyplot as plt


# Функция для получения входных данных от пользователя
def get_user_input(prompt, value_type=float):
    """
    Получение данных от пользователя с проверкой типа.

    :param prompt: Строка с запросом для пользователя
    :param value_type: Тип данных, который требуется
    :return: Значение, введенное пользователем
    """
    while True:
        try:
            return value_type(input(prompt))
        except ValueError:
            print("Ошибка: введите корректное число.")


# Ввод параметров для функции
coeffs = []
for i in range(1, 4):
    a = get_user_input(f"Введите коэффициент a{i}: ")
    b = get_user_input(f"Введите коэффициент b{i}: ")
    coeffs.append((a, b))

x_start = get_user_input("Введите начальное значение x: ")
x_end = get_user_input("Введите конечное значение x: ")
step = get_user_input("Введите шаг dx: ")

# Проверка корректности введенного шага
if step <= 0:
    print("Ошибка: шаг dx должен быть больше нуля.")
    exit()

# Генерация значений x
x_data = np.arange(x_start, x_end + step, step)


# Функция для вычисления значений y на основе x и коэффициентов
def calculate_function(x_vals, coeff_list):
    """
    Вычисляет значения y(x) для массива x с использованием заданных коэффициентов.

    :param x_vals: массив значений x
    :param coeff_list: список коэффициентов
    :return: массив значений y
    """
    y_total = np.zeros_like(x_vals)
    for a, b in coeff_list:
        y_total += a * np.sin(b * x_vals)
    return y_total


# Вычисление значений y
y_data = calculate_function(x_data, coeffs)

# Вывод таблицы значений x и y
print(f"{'x':<10} | {'y(x)':<10}")
print("-" * 25)
for x, y in zip(x_data, y_data):
    print(f"{x:<10.2f} | {y:<10.4f}")


# Функция для создания и сохранения графика
def plot_graph(x_vals, y_vals, filename="output_graph.png"):
    """
    Построение и сохранение графика функции.

    :param x_vals: массив значений x
    :param y_vals: массив значений y
    """
    plt.figure()
    plt.plot(x_vals, y_vals, label="y(x)")
    plt.title("График функции y(x)")
    plt.xlabel("x")
    plt.ylabel("y(x)")
    plt.grid(True)
    plt.legend()
    plt.savefig(filename)
    plt.show()


# Построение графика
plot_graph(x_data, y_data)
