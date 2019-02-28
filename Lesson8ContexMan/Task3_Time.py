
# Задача -3
# Создать менеджер контекста который будет подсчитывать время выполняния блока инсрукций

import time
import os


class ManageCont:
    def __init__(self, path, excep, is_suppress=False):
        self.path = path
        self.saved_cwd = None  # to save current dir
        self.excep = excep
        self.is_suppress = is_suppress
        self.start_time = 0

    def __enter__(self):
        self.start_time = time.time()
        self.saved_cwd = os.getcwd()
        try:
            os.chdir(self.path)
        except FileNotFoundError:
            print("Path '{}' is not correct.".format(self.path))

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.saved_cwd)
        print(time.time() - self.start_time)
        if exc_type is not None and issubclass(exc_type, self.excep):
            return self.is_suppress


with ManageCont(path="/Users/stas/PycharmProjects/PythonHomeworkDombrovskyi/", excep=KeyError, is_suppress=True):
    raise KeyError

