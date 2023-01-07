#  Реализовать базовый класс Worker (работник), в котором определить атрибуты:
#  name, surname, position (должность), income (доход). Последний атрибут должен
#  быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
#  например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на
#  базе класса Worker. В классе Position реализовать методы получения полного имени
#  сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
#  Проверить работу примера на реальных данных (создать экземпляры класса Position,
#  передать данные, проверить значения атрибутов, вызвать методы экземпляров).

wage = int(input("Введите заработную плату: "))
bonus = int(input("Введите премию: "))
income = {"wage": wage, "bonus": bonus}


class Worker:
    _income = income

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position


obj = Worker("Helen", "Rowling", "manager")
print(obj.surname)
print(obj._income)


class Position(Worker):
    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)

    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        total = self._income.get("wage") + self._income.get("bonus")
        print(total)


obj2 = Position("Helen", "Tsoy", "manager")
obj2.get_full_name()
obj2.get_total_income()
