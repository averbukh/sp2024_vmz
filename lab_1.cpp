#include <iostream>
#include <cmath>
#include <iomanip>
#include <vector>
#include <algorithm>

int main() {
    double a1, b1, a2, b2, a3, b3;
    double x0, xk, delta_x;

    // Ввод параметров
    std::cout << "Введите a1: ";
    std::cin >> a1;
    std::cout << "Введите b1: ";
    std::cin >> b1;
    std::cout << "Введите a2: ";
    std::cin >> a2;
    std::cout << "Введите b2: ";
    std::cin >> b2;
    std::cout << "Введите a3: ";
    std::cin >> a3;
    std::cout << "Введите b3: ";
    std::cin >> b3;
    std::cout << "Введите начальное значение x0: ";
    std::cin >> x0;
    std::cout << "Введите конечное значение xk: ";
    std::cin >> xk;
    std::cout << "Введите шаг Δx: ";
    std::cin >> delta_x;

    // Вычисление значений y и вывод их
    std::cout << std::fixed << std::setprecision(2);
    std::cout << "x\t\t y\n";
    for (double x = x0; x <= xk; x += delta_x) {
        double y = a1 * sin(b1 * x) + a2 * sin(b2 * x) + a3 * sin(b3 * x);
        std::cout << x << "\t " << y << "\n";
    }

    return 0;
