#  Реализовать базовый класс Worker (работник), в котором определить атрибуты:
#  name, surname, position (должность), income (доход). Последний атрибут должен
#  быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
#  например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на
#  базе класса Worker. В классе Position реализовать методы получения полного имени
#  сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
#  Проверить работу примера на реальных данных (создать экземпляры класса Position,
#  передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income

    def get_salary(self):
        wage = int(input("Введите заработную плату: "))
        bonus = int(input("Введите премию: "))
        self._income = {"wage": wage, "bonus": bonus}
        return self._income

# obj = Worker("Helen", "Rowling", "manager", {"wage": 2000, "bonus": 500})
# print(obj.surname)
# print(obj._income)
# obj.get_salary()
#
class Position(Worker):
    def __init__(self, name, surname, position, _income):
        super().__init__(name, surname, position, _income)

    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self, _income):
        wage = int(input("Введите заработную плату: "))
        bonus = int(input("Введите премию: "))
        total = self._income.get(wage)
        print(total)

obj2 = Position("Helen", "Tsoy", "manager", _income={"wage": 2000, "bonus": 500})
obj2.get_full_name()
obj2.get_total_income({"wage": 2000, "bonus": 500})
