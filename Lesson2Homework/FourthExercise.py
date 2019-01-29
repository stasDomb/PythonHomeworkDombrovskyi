

def array_function(array, n):
    if len(array) > n:
        result_number = array[n] ** n
        return result_number
    else: return -1

# array_example = [1,2,3,4,5,6,7]
# n = 3
# print(array_function(array_example,n))