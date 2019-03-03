# Задача-1
# Реализовать дескриптор валидации для аттрибута email.
# Ваш дескриптор должен проверять формат email который вы пытаетесь назначить

import re


class EmailDescriptor:

    def __init__(self, name="variable"):
        self.name = name

    def __get__(self, instance, owner):
        return instance.name

    def __set__(self, instance, value):
        if re.fullmatch("[\w-]+@[\w-]+\.[\w-]+", value):
            instance.name = value
        else:
            raise ValueError("it's not a valid email. Please, enter a valid email")


class MyClass:
    email = EmailDescriptor()


my_class = MyClass()
# my_class.email = "valid-email@gmail.com"
# print(my_class.email)
# my_class.email = "novalidemail"

