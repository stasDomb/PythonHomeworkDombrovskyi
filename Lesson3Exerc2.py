

def sum_array(array):
    sum_result = 0
    for i in range(0, len(array), 2):
           sum_result += array[i]
    return sum * (array[len(array) - 1])


array = [5, 15, 10, 25, 20, 100]
print(sum_array(array))
