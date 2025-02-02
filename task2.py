import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
def f(x):
    return x ** 2

a, b = 0, 2
n_points = 100000

def monte_carlo_integrate(func, a, b, n):

    x = np.random.uniform(a, b, n)
    y = np.random.uniform(0, func(b), n)

    points_under_curve = y < func(x)

    area_rectangle = (b - a) * func(b)
    ratio = np.sum(points_under_curve) / n
    integral = area_rectangle * ratio

    return integral, x, y, points_under_curve

mc_result, x_points, y_points, under_curve = monte_carlo_integrate(f, a, b, n_points)

exact_result, error = integrate.quad(f, a, b)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
x = np.linspace(-0.5, 2.5, 400)
y = f(x)
plt.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
plt.fill_between(ix, iy, color='gray', alpha=0.3)
plt.axvline(x=a, color='gray', linestyle='--')
plt.axvline(x=b, color='gray', linestyle='--')
plt.grid(True)
plt.title('Графік функції f(x) = x²')
plt.xlabel('x')
plt.ylabel('f(x)')

plt.subplot(1, 2, 2)
plt.scatter(x_points[~under_curve], y_points[~under_curve],
            color='red', alpha=0.1, label='Точки поза кривою')
plt.scatter(x_points[under_curve], y_points[under_curve],
            color='blue', alpha=0.1, label='Точки під кривою')
plt.plot(x, y, 'k-', linewidth=2)
plt.grid(True)
plt.title('Візуалізація методу Монте-Карло')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

plt.tight_layout()
plt.show()

print(f"Результат методу Монте-Карло: {mc_result:.6f}")
print(f"Точне значення інтеграла:    {exact_result:.6f}")
print(f"Абсолютна похибка:           {abs(mc_result - exact_result):.6f}")
print(f"Відносна похибка:            {abs(mc_result - exact_result) / exact_result * 100:.4f}%")