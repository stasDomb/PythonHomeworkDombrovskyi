#Задача -2
#Создать объект менеджера контекста который будет переходить
#  в папку которую он принимает на вход.
# Так же ваш объект должен принимать исключение которое он будет подавлять.
# Если флаг об исключении отсутствует, исключение должно быть поднято.
# Описать задачу выше но уже с использованием @contexmanager

import os
import contextlib


@contextlib.contextmanager
def manage_cont(path, excep, is_suppress=False):
    saved_cwd = os.getcwd()
    try:
        os.chdir(path)
        yield {}
    except excep:
        print("Exception '{}' was raised".format(excep))

    finally:
        os.chdir(saved_cwd)
        if is_suppress:
            pass
        else:
            raise


with manage_cont(path="/Users/stas/PycharmProjects/PythonHomeworkDombrovskyi/", excep=KeyError,is_suppress=True) as mc:
    raise KeyError


