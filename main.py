import pulp

# Створення моделі (максимізація)
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні: кількість лимонаду (L) і фруктового соку (F)
L = pulp.LpVariable("Lemonade", lowBound=0, cat="Integer")
F = pulp.LpVariable("FruitJuice", lowBound=0, cat="Integer")

# Цільова функція: максимізуємо загальну кількість вироблених продуктів
model += L + F, "Total_Production"

# Обмеження ресурсів
model += 2 * L + 1 * F <= 100, "Water_Limit"
model += 1 * L <= 50, "Sugar_Limit"
model += 1 * L <= 30, "Lemon_Juice_Limit"
model += 2 * F <= 40, "Fruit_Puree_Limit"

# Розв'язання задачі
model.solve()

# Виведення результатів
print("Кількість виробленого лимонаду:", int(L.varValue))
print("Кількість виробленого фруктового соку:", int(F.varValue))