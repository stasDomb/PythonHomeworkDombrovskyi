# Создать объект менеджера контекста который будет переходить
#  в папку которую он принимает на вход.
# Так же ваш объект должен принимать исключение которое он будет подавлять.
# Если флаг об исключении отсутствует, исключение должно быть поднято.


import os


class ManageCont:
    def __init__(self, path, excep, is_suppress=False):
        self.path = path
        self.saved_cwd = None  # to save current dir
        self.excep = excep
        self.is_suppress = is_suppress

    def __enter__(self):
        self.saved_cwd = os.getcwd()
        try:
            os.chdir(self.path)
        except FileNotFoundError:
            print("Path '{}' is not correct.".format(self.path))

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.saved_cwd)
        if exc_type is not None and issubclass(exc_type, self.excep):
            return self.is_suppress


with ManageCont(path="/Users/stas/PycharmProjects/PythonHomeworkDombrovskyi/", excep=KeyError):
    raise KeyError

