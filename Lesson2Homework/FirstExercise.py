
from collections import defaultdict
from itertools import groupby

data = [
    {'name': 'Viktor', 'city': 'Kiev', 'age': 30 },
    {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
    {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
    {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
    {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
    {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]


def sort_age(data):
    #data.get("age")
    data.sort(key=lambda k: k["age"])
    print(data)

# 1.1 sorted dictionary by age
print(sort_age(data))

# 1.2 grouped dictionary by city


def group_by_city(data_dict):
    grouped_result = {}
    for i in data_dict:
        city_name = i.get("city")
        if city_name in grouped_result:
            grouped_result[city_name].append({"name": i.get("name"), "age": i.get("age")})
        else:
            grouped_result[city_name] = [{"name": i.get("name"), "age": i.get("age")}]
    return  grouped_result


print(group_by_city(data))

