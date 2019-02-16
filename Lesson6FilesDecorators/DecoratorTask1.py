# Задача-3 - не обязательна к выполнению
# Написать декоратор который будет подавлять ошибки возникающие в теле вашей функции.


def suppress_err(func):
    def wrapper():
        try:
            func()
        except ValueError as e:
            pass
    return wrapper


@suppress_err
def my_func():
    raise ValueError("some text error")


my_func()
