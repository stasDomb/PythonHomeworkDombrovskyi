# Задача-4
# Изменить исходную строку на новую строку в которой первый и последний символы строки поменяны местами.


def modify_string(example_string):
    the_begin = example_string[:1]
    the_end = example_string[len(example_string) - 1:]
    new_string = the_end + example_string[1:] + the_begin
    return new_string


example_string = "How. are you? Eh, ok. Low or Lower? Ohhh."
print(modify_string(example_string))
