
from collections import defaultdict
from itertools import groupby

data = [
    {'name': 'Viktor', 'city': 'Kiev', 'age': 30 },
    {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
    {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
    {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
    {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
    {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]


def sort_age(age):
    return age.get("age")


# 1.1 sorted dictionary by age
print(sorted(data, key=sort_age))

# 1.2 grouped dictionary by city

# GroupedData = {}
# for key, value in sorted(data.iteritems()):
#    GroupedData[value].append(key)

for g in groupby(sorted(data, key=lambda x:x[1]), key=lambda x:x[1]):
    print(g[0])
    for i in g[1]:
        print(' - ', i)



