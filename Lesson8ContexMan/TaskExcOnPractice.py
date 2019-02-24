#Определить свой класс Exception
# который будет записывать месседж ошибки в файл.
# Тоесть при возникновении ошибки
# вам нужно писать ее в файл а не выводить.
# Как пример вызова вашего функционала используйте пример ниже:

#try:
#     some_func()
# except FormatError as exc:
#     exc.logerror()


class SomeError(Exception):

    def __init__(self, line, file):
        # line, file - where is exception was happened
        self.line = line
        self.file = file

    def write_log_to_file(self, logfile='file.txt'):
        with open(logfile, 'a') as log_f:
            log_f.write("Error at file {} in {}", self.file, self.line, file =log)


def test_func():
    raise SomeError(40, "compas.txt")


try:
    test_func()
except SomeError as exc:
    exc.write_log_to_file()


