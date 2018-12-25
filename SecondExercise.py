
from collections import defaultdict

def most_frequent(list_var):

    # your code is here
    str_counter_dict = defaultdict(int)
    result_dict = {}
    for str_dict in list_var:
        str_counter_dict[str_dict] += 1
        result_dict.update({str_counter_dict[str_dict]: str_dict})
#    print(result_dict)
    return result_dict.get(max(result_dict.keys()))


# list_example = ("asd","asd","dsa","dsa","dewq","dwwr","dsa")
# most_frequent(list_example)

