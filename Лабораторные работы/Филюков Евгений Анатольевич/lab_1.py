import numpy as np
import matplotlib.pyplot as plt

def get_user_input(prompt, type_=float):
    """Функция для получения ввода от пользователя с обработкой ошибок."""
    while True:
        try:
            return type_(input(prompt))
        except ValueError:
            print("Ошибка ввода! Попробуйте снова.")

# Получение параметров от пользователя
params = {}
for param in ["a1", "b1", "a2", "b2", "a3", "b3"]:
    params[param] = get_user_input(f"Введите {param}: ")

x0 = get_user_input("Введите начальное значение x (x0): ")
xk = get_user_input("Введите конечное значение x (xk): ")
dx = get_user_input("Введите шаг Δx: ")

# Создание массива значений x с шагом dx
x_values = np.arange(x0, xk + dx, dx)

# Вычисление значений y(x)
y_values = (
    params["a1"] * np.sin(params["b1"] * x_values)
    + params["a2"] * np.sin(params["b2"] * x_values)
    + params["a3"] * np.sin(params["b3"] * x_values)
)

# Отображение таблицы значений x и y
print("\nТаблица значений x и y:")
print(f"{'x':>10} {'y':>10}")
for x, y in zip(x_values, y_values):
    print(f"{x:>10.4f} {y:>10.4f}")

# Построение графика
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label='y(x)', color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции y(x)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()
