
import matplotlib.pyplot as plt
import numpy as np

print("Введите координату точки отсчёта:")
x0 = float(input())
print("Введите погрешность:")



def method(f1, x0, fault=0.001, max_iter=100):
    iter_count = 0
    while iter_count < max_iter:
        y0 = f1(x0)
        x1 = - (y0 + 2) / (2)
        if abs(x1 - x0) < fault:
            break
        print(x1)
        x0 = x1
        iter_count += 1
    return x0 , iter_count

def f1(x):
    return x ** 3

def f2(x):
    return (-2) * x - 2

solution, iterations = method(f1, x0)

print("Корень уравнения:", solution)
print("Количество итераций:", iterations)
print("Значение функции:")