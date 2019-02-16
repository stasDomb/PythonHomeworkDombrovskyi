# Задача-1
# Из текстового файла удалить все слова, содержащие от трех до пяти символов,
# но при этом из каждой строки должно быть удалено только четное количество таких слов.


with open("./file.txt") as f_in:
    array_of_file = [row.strip() for row in f_in]
    result_in_file = []
    for words in array_of_file:
        counter_hits = 0

        every_line = words.split(' ')

        # для каждой строки находим слова, которые нас интересуют
        excluded_words = list(filter(lambda x: 2 < len(x) < 6, every_line))

        # узнаем сколько таких слов
        counter_hits = len(excluded_words)

        # если таких слов нечетное количество, то уменьшаем счетчик, чтобы удалить на 1 слово меньше
        if counter_hits % 2 != 0:
            counter_hits -= 1

        # приступаем к удалению
        for word in every_line:
            if word in excluded_words and counter_hits > 0:
                every_line.remove(word)
                counter_hits -= 1

        #  добавляем к результирующему списку очередную подернизированную строку
        result_in_file.append(every_line)

    # записываем в файл
    with open('./file.txt', 'w') as f_out:
        for line in result_in_file:
            f_out.write(" ".join(line) + "\n")
