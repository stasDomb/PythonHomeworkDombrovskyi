

array = [1, 3, 6, 4, 1, 2, -3, -10]


positive_array = []
for a in array:
    if a > 0:
        if a not in positive_array:
            positive_array.append(a)
# if original array doesn't have any positive numbers:
if positive_array == []:
    print("incorrect statement")
    # need to sort the array

positive_array.sort()

    # create array for comparing
list_for_compare = list(range(1, len(positive_array) + 1))

#for i in list_for_compare:
for index, element in enumerate(list_for_compare):
    print(str(list_for_compare[index]) + " plus " + str(positive_array[index]))
    if not list_for_compare[index] == positive_array[index]:
        print(list_for_compare[index])


