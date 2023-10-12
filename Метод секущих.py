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
    c1 = a

    x_history = [b]
    y_history = [f(b)]
    while True:
        a_values = f(a)
        b_values = f(b)
        c2 = (a_values * b - a * b_values) / (a_values - b_values)
        c_values = f(c2)
        m.append(1)
        print(c2)
        print(f(c2))
        x_history.append(c2)
        y_history.append(c_values)

        if abs(c1 - c2) < fault:
            break
        if (a_values < 0 and c_values > 0) or (a_values > 0 and c_values < 0):
            b = c2
        else:
            a = c2
        c1 = c2

    x = [i / 10 for i in range(-100, 100)]
    y = [f(x_val) for x_val in x]
    plt.plot(x, y, label='f(x)', color='blue')

    for i in range(len(x_history) - 1):
        x_curr = x_history[i]
        y_curr = y_history[i]
        plt.plot([x_curr, x_curr], [0, y_curr], 'r--')
        plt.plot([x_curr, a], [y_curr, f(a)], 'g-')

    plt.scatter(c2, c_values, color='red', label='Root')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

    return c2


def F(x): return e * x ** 3 + g * x ** 2 + c * x + d


root = find_root(F, a, b, fault) + 10 * fault
print("Корень уравнения:", root)
print("Количество иттераций:", len(m) - 1)
print("Значение функции:", F(root))
