"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие
атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость
автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        print(f'Машина {self.name} поехала.')
    def stop(self):
        print(f'Машина {self.name} остановилась.')
    def turn(self, direction):
        self.direction = 'налево' if direction == 0 else 'направо'
        print(f'Машина {self.name} повернула {self.direction}.')
    def show_speed(self):
        print(f'Скорость автомобиля: {self.name} - {self.speed} км/ч.')

class TownCar(Car):
    def show_speed(self):
        print(f'Текущая скорость автомобиля: {self.name} - {self.speed} км/ч.' if self.speed<=60
        else f'Скорость автомобиля {self.name} превышает допустимую скорость на {self.speed - 60} км/ч.')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        print(f'Текущая скорость автомобиля: {self.name} - {self.speed} км/ч.' if self.speed<=40
        else f'Скорость автомобиля {self.name} превышает допустимую скорость на {self.speed - 40} км/ч.')

class PoliceCar(Car):
    pass

towncar = TownCar(100, 'красный', 'Nissan Juke', False)
print(f'Автомобиль - {towncar.name}, {towncar.color}, текущая скорость передвижения: {towncar.speed} км/ч.')
towncar.go()
towncar.turn(1)
towncar.stop()
towncar.show_speed()

sportcar = SportCar(170, 'красный', 'Ferrari', False)
print(f'Автомобиль - {sportcar.name}, {sportcar.color}, текущая скорость передвижения: {sportcar.speed} км/ч.')
sportcar.go()
sportcar.turn(1)
sportcar.stop()
sportcar.show_speed()

workcar = WorkCar(50, 'красный', 'Caterpillar', False)
print(f'Автомобиль - {workcar.name}, {workcar.color}, текущая скорость передвижения: {workcar.speed} км/ч.')
workcar.go()
workcar.turn(1)
workcar.stop()
workcar.show_speed()

policecar = PoliceCar(220, 'желтый', 'Жигули', True)
print(f'Автомобиль - {policecar.name}, {policecar.color}, текущая скорость передвижения: {policecar.speed} км/ч.')
policecar.go()
policecar.turn(0)
policecar.stop()
policecar.show_speed()