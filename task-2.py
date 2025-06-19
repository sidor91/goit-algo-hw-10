import numpy as np
from scipy.integrate import quad

# Визначення функції
def f(x):
    return x ** 2

# Межі інтегрування
a = 0
b = 2

# Метод Монте-Карло
N = 100_000  # Кількість випадкових точок
x_rand = np.random.uniform(a, b, N)
y_rand = f(x_rand)
monte_carlo_result = (b - a) * np.mean(y_rand)

# Аналітичне обчислення інтеграла через scipy
analytical_result, _ = quad(f, a, b)

# Виведення результатів
print(f"Метод Монте-Карло (N={N}): {monte_carlo_result:.5f}")
print(f"Аналiтичне значення:        {analytical_result:.5f}")
print(f"Абсолютна похибка:          {abs(monte_carlo_result - analytical_result):.5f}")

"""
Висновок:
	•	Метод Монте-Карло дає наближення, яке стає точнішим при збільшенні кількості точок (N).
	•	Для N = 100_000 результат дуже близький до точного аналітичного значення.
	•	Метод Монте-Карло особливо корисний для багатовимірних або складних функцій, де аналітичне обчислення складне або неможливе.
"""