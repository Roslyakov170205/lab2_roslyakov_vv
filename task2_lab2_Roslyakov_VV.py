# Исходные данные
reserve_funds = 20000  # Финансовая подушка
monthly_income = 5000  # Ежемесячный доход
monthly_expenses = 6000  # Начальные траты
price_growth = 0.05  # Процент роста цен за месяц

months_survived = 0  # Счётчик месяцев, которые можно прожить без долгов
remaining_funds = []  # Список для отслеживания остатка подушки

while reserve_funds >= 0:
    # Покрытие расходов: сначала зарплата, потом резерв
    reserve_funds += monthly_income - monthly_expenses
    months_survived += 1
    # Увеличение расходов на следующий месяц
    monthly_expenses *= (1 + price_growth)
    # Если подушка ещё не исчерпана, записываем её значение
    if reserve_funds >= 0:
        remaining_funds.append(reserve_funds)

# Вывод результатов
print("Количество месяцев, которые можно прожить без долгов:", len(remaining_funds))
