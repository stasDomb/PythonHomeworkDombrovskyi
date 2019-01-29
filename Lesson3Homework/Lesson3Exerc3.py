# Задача-3
# Дана строка и нужно найти ее первое слово.
# При решении задачи обратите внимание на следующие моменты:
#   1)В строке могут встречатся точки и запятые
#   2)Строка может начинаться с буквы или, к примеру, с пробела или точки
#   3)В слове может быть апостроф и он является частью слова
#   4)Весь текст может быть представлен только одним словом и все


def search_first_word(example_string):
    separated_string = example_string.split()
    # to know when word starts
    counter = 0
    for l in separated_string[0]:
        if l.isalpha() == 0:
            counter += 1
        else:
            break
    first_word_inprocess = separated_string[0][counter:]
    # search for the remaining part of the word(including "'")
    counter = 0
    for l in first_word_inprocess:
        if l.isalpha():
            counter += 1
        else:
            if l == "'":
                counter += 1
            else:
                break
    first_word = first_word_inprocess[:counter]
    return first_word



example_string = ".S'How. are you? Eh, ok. Low or Lower? Ohhh."
print(search_first_word(example_string))

#alternative solution
#s = s.replace('.', '')
#s = s.replace(',', '')
#s = s.strip()
#new_s = s.split(' ')[0]
