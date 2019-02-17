# TASK-1
# Write a function:
# def solution(A)
# that, given an array A of N integers,
# returns the smallest positive integer (greater than 0) that does not occur in A.
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# Given A = [1, 2, 3], the function should return 4.
# Given A = [−1, −3], the function should return 1.
# Assume that:
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].


def search_in_array(array):
    """This function search in array the smallest positive integer that doesn't occur in the array"""
    # at first, keep only positive part of array and get ride of duplicates
    positive_array = []
    for a in array:
        if a > 0:
            if a not in positive_array:
                positive_array.append(a)
    # if original array doesn't have any positive numbers:
    if positive_array == []:
        return 1
    # need to sort the array

    positive_array.sort()

    # create array for comparing
    list_for_compare = list(range(1, len(positive_array) + 1))
#    for i in list_for_compare:
#        if not list_for_compare[i] == positive_array[i-1]:
#            return list_for_compare[i-1]
    for index, element in enumerate(list_for_compare):
        if not list_for_compare[index] == positive_array[index]:
             return list_for_compare[index]



example_array = [1, 3, 6, 4, 1, 2, -3, -10]
# example_array = [1,5,2,3,4]
# create array for comparing
print(search_in_array(example_array))
