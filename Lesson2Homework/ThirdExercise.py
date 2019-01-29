
int_number = input()

def mult_digits(int_number):
    mult = 1
    for i in int_number:
        if int(i):
            mult *= int(i)

    return mult

print(mult_digits(int_number))