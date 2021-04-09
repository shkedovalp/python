#2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

#вариант 1
def person_info(**kwargs):
    print(list(kwargs.values()))

person_info(name = 'Вася', surname = 'Иванов',
            age = '1981г.', city = 'Самара',
            email = 'IvanovV@gmail.com',
            number = 'тел. 890678945')

#вариант 2
def person_info(**kwargs):
    return (list(kwargs.values()))

result = person_info(name = input('Введите ваше имя: '),
              surname = input('Введите вашу фамилию: '),
              age = input('Введите Ваш год рождения: '),
              city = input('Введите Ваш город проживания: '),
              email = input('Введите Ваш email-адрес: '),
              number = input('Введите Ваш телефон: '))
print(result)


#вариант 3
def person_info(name, surname, age, city, email, number):
    result = f'{name}, {surname}, {age} года рождения, проживающий в городе {city}, email-адрес: {email}, телефон - {number}'
    return result

print(person_info('Вася', 'Иванов', '1981', 'Самара', 'IvanovV@gmail.com', '8905990777'))
