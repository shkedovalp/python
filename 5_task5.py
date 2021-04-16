"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле
и выводить ее на экран.
"""
from random import randint

with open('text5.txt', 'w') as my_file:
    my_list = [randint(0, 50) for i in range(5)]
    my_file.write(' '.join(map(str, my_list)))
print(f'Сумма чисел в файле: {sum(my_list)}')