from pulp import *

prob = LpProblem("Оптимізація_виробництва_напоїв", LpMaximize)

# Визначаємо змінні
lemonade = LpVariable("Лимонад", 0, None, LpInteger)
fruit_juice = LpVariable("Фруктовий_сік", 0, None, LpInteger)

prob += lemonade + fruit_juice, "Загальна кількість напоїв"

prob += 2 * lemonade + fruit_juice <= 100, "Обмеження_води"

prob += lemonade <= 50, "Обмеження_цукру"

prob += lemonade <= 30, "Обмеження_лимонного_соку"

prob += 2 * fruit_juice <= 40, "Обмеження_фруктового_пюре"

prob.solve()


print("Статус:", LpStatus[prob.status])
print("\nОптимальні значення виробництва:")
print(f"Лимонад: {int(value(lemonade))} одиниць")
print(f"Фруктовий сік: {int(value(fruit_juice))} одиниць")
print(f"\nЗагальна кількість вироблених напоїв: {int(value(lemonade + fruit_juice))} одиниць")

print("\nВикористання ресурсів:")
print(f"Вода: {2*value(lemonade) + value(fruit_juice)}/100 одиниць")
print(f"Цукор: {value(lemonade)}/50 одиниць")
print(f"Лимонний сік: {value(lemonade)}/30 одиниць")
print(f"Фруктове пюре: {2*value(fruit_juice)}/40 одиниць")