# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите,
# с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
# или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете
# на одного сотрудника.


revenue = int(input('Введите вручку в рублях за текущий период: - '))
costs = int(input('Введите издежки в рублях: - '))
if revenue > costs:
    profit = revenue - costs
    ren = int(profit * 100 / revenue)
    print(f'Поздравляем! В текущем периоде прибыль Вашей фирмы составила {profit} рублей. Рентабельность - {ren} процентов.')
    employees = int(input('Введите количество сотрудников - '))
    profit_employees = profit / employees
    print(f'Прибыль в расчете на одного сотрудника составила {profit_employees} рублей')

elif costs > revenue:
    print('Хьюстон, у Вас проблемы... Ваша фирма работает в убыток! Пора принять меры!')

elif revenue == costs:
    print('Думал заработать, ан нет, снова опыт...')

print('end')

