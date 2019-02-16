# Задача-4 - не обязательна к выполнению
# Написать декоратор c аргументом который будет подавлять
# определенные ошибки возникающие в теле вашей функции.
# Ошибки которые должен будет подавить ваш
# декоратор вы должны передать ему в качестве аргумента


errors = [ValueError, NameError, TypeError]


def decorator_with_arg(*args):
    def suppress_err(func):
        def wrapper():
            try:
                func()
            except ValueError as e:
                if isinstance(e, args):
                    pass
                else:
                    print(e)
        return wrapper
    return suppress_err


@decorator_with_arg(*errors)
def my_func():
    raise ValueError("One of the three errors")


my_func()





