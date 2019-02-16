# Задача-1
# У вас есть список(list) IP адрессов. Вам необходимо создать
# класс который будет иметь методы:
# 1) Получить список IP адресов
# 2) Получить список IP адресов в развернутом виде
# (10.11.12.13 -> 13.12.11.10)
# 3) Получить список IP адресов без первых октетов
# (10.11.12.13 -> 11.12.13)
# 4) Получить список последних октетов IP адресов
# (10.11.12.13 -> 13)


class ClassForIpAd(object):

    def __init__(self, value):
        self._value = value

    def get_list_ip(self):
        return self._value

    def get_list_reverse_ip(self):
        result = []
        for ip in self._value:
            result.append('.'.join(ip.split('.')[::-1]))
        return result

    def get_ip_wo_1_oct(self):
        result = []
        for ip in self._value:
            result.append('.'.join(ip.split('.')[1:]))
        return result

    def get_last_oct(self):
        result = []
        for ip in self._value:
            result.append(ip.split('.')[-1])
        return result
