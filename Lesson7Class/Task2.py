# Задача-2
# У вас несколько JSON файлов. В каждом из этих файлов есть
# произвольная структура данных. Вам необходимо написать
# класс который будет описывать работу с этими файлами, а
# именно:
# 1) Запись в файл
# 2) Чтение из файла
# 3) Объединение данных из файлов в новый файл
# 4) Получить путь относительный путь к файлу
# 5) Получить абсолютный путь к файлу


import json
import os
from pathlib import Path


class ClassForJson(object):

    @staticmethod
    def write_to_file(file, data):
        with open(file, "w") as write_file:
            json.dump(data, write_file)

    @staticmethod
    def read_from_file(file):
        try:
            with open(file, "r") as f:
                data = json.load(f)
                return data

        except FileNotFoundError:
            print("File '{}' not found.".format(file))

    def merge_files(self, new_common_file, *args):
        result = []
        for f in args:
            result.append(self.read_from_file(f))
        result_to_write = list(filter(lambda x: x is not None, result))
        self.write_to_file(new_common_file, result_to_write)

    @staticmethod
    def relative_path(file):
        return os.path.relpath(file)

    @staticmethod
    def abs_path(file):
        return Path(file).resolve()

