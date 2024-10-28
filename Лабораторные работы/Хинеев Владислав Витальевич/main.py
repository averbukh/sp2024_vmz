from math import sin
import matplotlib.pyplot as plt

arr = input('Введите данные в таком порядке через пробел: a1, b1, a2, b2, a3, b3, x0, xk, Δx: ').split()
arr = [int(n) for n in arr]

def func(a1, b1, a2, b2, a3, b3, start, end, step):
    arrX, arrY = [], []
    print(f"{'x':<10}{'y':<10}")
    for x in range(start, end + 1, step):
        y = a1 * sin(b1 * x) + a2 * sin(b2 * x) + a3 * sin(b3 * x)

        print(f"{x:<10.2f}{y:<10.2f}")

        arrX.append(x)
        arrY.append(y)
    return arrX, arrY

def build_schedule(arrX, arrY):
    plt.plot(arrX, arrY, label='y(x)', color='b')
    plt.title('y(x) = a1 * sin(b1 * x) + a2 * sin(b2 * x) + a3 * sin(b3 * x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.grid()
    plt.legend()

    # plt.show()
    plt.savefig('graph.png')

build_schedule(*func(*arr))