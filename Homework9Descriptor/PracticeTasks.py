
class Kilometers:

    def __get__(self, instance, owner):
        return instance.m/1000

    def __set__(self, instance, value):
        instance.m =value/1000


class Distance:
    kilometers = Kilometers()

    def __init__(self, m):
        self.m = m


distance = Distance(1200)

print(distance.kilometers)
print(distance.m)

distance.m = 2200
print(distance.kilometers)