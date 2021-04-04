# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a
# километров. Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
#
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.


a = int(input('Сколько километров вы пробежали сегодня? - '))
b = int(input('Сколько километров вы желаете пробегать? - '))
day = 1
while b - a >= 0:
    a = a + a * 0.1
    day = day + 1
print(f'Увеличивая дистанцию на 10% в день, вы достигнете результата на {day} -й день тренировок.')

