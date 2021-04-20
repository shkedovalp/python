"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов,
вызвать методы экземпляров).

"""

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = f'Должность: {position}'
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        return f'Полное имя сотрудника: {self.name} {self.surname}'
    def get_total_incom(self):
        return f'Доход с учетом премии составляет: {sum(self._income.values())} рублей.'

person_1 = Position('Питонов', 'Питон', 'инженер', 10000, 200)
print(person_1.get_full_name())
print(person_1.position)
print(person_1.get_total_incom())

person_2 = Position('Вреднов', 'Лавр', 'сметчик', 50000, 1000)
print(person_2.get_full_name(), person_2.position, person_2.get_total_incom(), sep='\n')
