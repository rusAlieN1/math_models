import matplotlib.pyplot as plt
import numpy as np

print("Введите коэффициент кубического уравнения при x^3:")
a = float(input())
print("Введите коэффициент кубического уравнения при x^2:")
b = float(input())
print("Введите коэффициент кубического уравнения при x:")
c = float(input())
print("Введите свободный коэффициент кубического уравнения:")
d = float(input())
print("Введите координату точки отсчёта:")
x0 = float(input())
print("Введите погрешность:")


def method(f, df, x0, fault=float(input()), max_iter=100):
    iter_count = 0
    x_history = [x0]
    y_history = [f(x0)]

    while iter_count < max_iter:
        x1 = x0 - f(x0) / df(x0)
        if abs(x1 - x0) < fault:
            break
        x_history.append(x1)
        y_history.append(f(x1))
        x0 = x1
        iter_count += 1
        print(x1, f(x1))

    x = np.arange(-5.00, 8.00, 0.1)
    y = [f(x_val) for x_val in x]
    plt.plot(x, y, label='f(x)', color='blue')

    for i in range(len(x_history) - 1):
        x_curr = x_history[i]
        y_curr = y_history[i]
        x_next = x_history[i + 1]
        y_next = y_history[i + 1]
        plt.plot([x_curr, x_curr], [0, y_curr], 'r--')
        plt.plot([x_curr, x_next], [y_curr, 0], 'g-')

    plt.scatter(x1, f(x1), color='red', label='Root')

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

    return x1, iter_count


def f(x):
    return a * x ** 3 + b * x ** 2 + c * x + d


def df(x):
    return 3 * a * x ** 2 + 2 * b * x + c


solution, iterations = method(f, df, x0)

print("Корень уравнения:", solution)
print("Количество итераций:", iterations)
print("Значение функции:", f(solution))
