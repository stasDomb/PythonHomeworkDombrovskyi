# Задача-3
# реализовать дескриптор IngegerField(), который будет хранить уникальные
# состояния для каждого класса где он объявлен


class IngegerField:
    instances = {}

    def __init__(self, value=None):
        self.instances[self] = value

    def __get__(self, instance, owner):
        return self.instances[self, instance]

    def __set__(self, instance, value):
        self.instances[self, instance] = value


class Data:
    number = IngegerField()


data_row = Data()
new_data_row = Data()

data_row.number = 5
new_data_row.number = 10

assert data_row.number != new_data_row.number
