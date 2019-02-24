#Задача -2
#Создать объект менеджера контекста который будет переходить
#  в папку которую он принимает на вход.
# Так же ваш объект должен принимать исключение которое он будет подавлять.
# Если флаг об исключении отсутствует, исключение должно быть поднято.
# Описать задачу выше но уже с использованием @contexmanager

import os
import contextlib


@contextlib.contextmanager
def manage_cont(path,excep):
    saved_cwd = os.getcwd()
    try:
        os.chdir(path)
    except FileNotFoundError:
        print("Path '{}' is not correct.".format(path))
    try:
        yield {}
    except excep as e:
        print("error: {}".format(e))
    finally:
        os.chdir(saved_cwd)
        return excep


with manage_cont(path="/Users/stas/PycharmProjects/PythonHomeworkDombrovskyi/", excep=KeyError) as mc:
    raise KeyError


