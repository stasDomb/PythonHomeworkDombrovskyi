# Задача-2
# Текстовый файл содержит записи о телефонах и их владельцах.
# Переписать в другой файл телефоны тех владельцев, фамилии которых начинаются с букв К и С.


def extract_info(file_input, file_output):
    with open(file_output, 'w') as f_out:
        with open(file_input, 'r') as f_in:
            for line in f_in:
                words = line.split()
                if words[0].startswith('K', 'C'):
                    f_out.write(words[1] + '\n')


extract_info('./source_file.txt', './res_file.txt',)
