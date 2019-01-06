# Задача-5
# Дан тапл(tuple), необходимо его конвертнуть в стринг.
# Например:
# ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's') == 'exercises


def modify_tuple_to_str(example_tuple):
    result_string = ""
    for i in example_tuple:
        result_string += i
    return result_string


example_tuple = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
print(modify_tuple_to_str(example_tuple))


#alternative solution
#solution: return ''.join(tup)
