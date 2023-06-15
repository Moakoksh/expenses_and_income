def calculate_balance():
    total_income = 0
    total_expenses = 0

    # Ввод доходов
    income = float(input("Введите доходы (введите 0 для завершения): "))
    while income != 0:
        total_income += income
        income = float(input("Введите доходы (введите 0 для завершения): "))

    # Ввод расходов
    expense = float(input("Введите расходы (введите 0 для завершения): "))
    while expense != 0:
        total_expenses += expense
        expense = float(input("Введите расходы (введите 0 для завершения): "))

    # Расчет и вывод баланса
    balance = total_income - total_expenses
    print("Общий доход:", total_income)
    print("Общие расходы:", total_expenses)
    print("Баланс:", balance)


# Вызов функции для запуска калькулятора расходов и доходов
calculate_balance()
