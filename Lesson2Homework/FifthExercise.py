
str_example = "asd fsdf 1923 asd fdg asda 9231 921 gfrs"
str_example1 = "asd fsdf 1923 asd fdg asda sss dddd 9231 921 gfrs"

def search_in_str(str1):
    count = 0
    for w in str1.split():
        if w.isalpha():
            count += 1
        else:
            if count == 3:
                return True
            count = 0

    return False



print(search_in_str(str_example))
