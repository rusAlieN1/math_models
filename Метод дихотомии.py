import matplotlib.pyplot as plt

m = []
print("Введите координату 1 точки отсчёта:")
a = float(input())
print("Введите координату 2 точки отсчёта:")
b = float(input())
print("Введите коэффициент кубического уравнения при x^3:")
e = float(input())
print("Введите коэффициент кубического уравнения при x^2:")
g = float(input())
print("Введите коэффициент кубического уравнения при x:")
c = float(input())
print("Введите свободный коэффициент кубического уравнения:")
d = float(input())

print("Введите погрешность:")
fault = float(input())


def find_root(f, a, b, fault):
    if (f(a) * f(b) >= 0):
        raise Exception("Initial approximation error")
    prev_c = None

    x_history = []
    y_history = []

    while True:
        c = (a + b) / 2
        a_values = f(a)
        c_values = f(c)
        m.append(1)
        print(c, f(c))
        x_history.append(c)
        y_history.append(c_values)

        if prev_c is not None and abs(c - prev_c) <= fault:
            break
        if a_values * c_values < 0:
            b = c
        else:
            a = c
        prev_c = c

    x = [i / 10 for i in range(-50, 71)]
    y = [f(x_val) for x_val in x]
    plt.plot(x, y, label='f(x)', color='blue')

    for i in range(len(x_history) - 1):
        x_curr = x_history[i]
        y_curr = y_history[i]
        plt.plot([x_curr, x_curr], [0, y_curr], 'r--')  # Опускаем перпендикуляр

    plt.scatter(c, c_values, color='red', label='Root')

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

    return c


def F(x):
    return e * x ** 3 + g * x ** 2 + c * x + d


root = find_root(F, a, b, fault)
print("Корень уравнения:", root)
print("Количество итераций:", len(m) - 1)
print("Значение функции:", F(root))
