# Задача-2
# Дан массив целых чисел. Нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд),
# затем перемножить эту сумму и последний элемент исходного массива.
# Не забудьте, что первый элемент массива имеет индекс 0.


def sum_array(array):
    sum_result = 0
    for i in range(0, len(array), 2):
           sum_result += array[i]
    return sum * (array[len(array) - 1])


array = [5, 15, 10, 25, 20, 100]
print(sum_array(array))
