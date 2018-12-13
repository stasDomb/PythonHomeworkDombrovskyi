
str_example = "asd fsdf 1923 asd fdg asda 9231 921 gfrs"


def search_in_str(str1):
    count = 0
    for w in str1.split():
        if w.isalpha():
            count += 1
            if count == 3:
                return True
        else:
            count = 0
    return False



print(search_in_str(str_example))
