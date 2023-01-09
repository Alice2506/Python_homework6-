#  Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
#  speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
#  которые должны сообщать, что машина поехала, остановилась, повернула (куда).
#  Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
#  Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость
#  автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении
#  скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    speed = 90
    color = "red"
    name = "Lexus"
    is_police = False
    direction = "налево"

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self):
        self.direction = input("Укажите направление: ")
        print(f'Автомобиль поворачивает {self.direction}')

    def show_speed(self):
        print(f'Текущая скорость: {self.speed} км/ч')

# obj = Car()
# obj.show_speed()
class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Скорость выше допустимой")
        else:
            print(f'Текущая скорость: {self.speed} км/ч')

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Скорость выше допустимой")
        else:
            print(f'Текущая скорость: {self.speed} км/ч')

class    PoliceCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Скорость выше допустимой")
        else:
            print(f'Текущая скорость: {self.speed} км/ч')

obj = WorkCar()
obj.show_speed()