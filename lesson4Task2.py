
# A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones
# at both ends in the binary representation of N.
# For example, number 9 has binary representation 1001 and contains a binary gap of length 2.
# The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3.
# The number 20 has binary representation 10100 and contains one binary gap of length 1.
# The number 15 has binary representation 1111 and has no binary gaps.
# The number 32 has binary representation 100000 and has no binary gaps.
#
# Write a function:
#
# def solution(N)
#
# that, given a positive integer N, returns the length of its longest binary gap.
# The function should return 0 if N doesn't contain a binary gap.
#
# For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.
# Assume that:
# N is an integer within the range [1..2,147,483,647]


def max_binary_gap(number):
    binary_view = str(bin(number)[2:])
    max_gap_length = 0
    cur_gap_length = 0
    for i in range(len(binary_view)):
        # if number & (1 << i):
        if binary_view[i] == "0":
            # Not set, the gap widens.
            cur_gap_length += 1

        else:
            # Set, any gap is over
            if cur_gap_length > max_gap_length:
                max_gap_length = cur_gap_length
            cur_gap_length = 0
    if cur_gap_length > max_gap_length:
        max_gap_length = cur_gap_length
    # for cases where only "1"
#    if cur_gap_length == 0:
 #       return 0


    return  max_gap_length

    # binary_view = bin(number)
    # for i in binary_view[2:]:
    #    print(i)
    # return bin(number)


print(max_binary_gap(3))
number = 3
#print(bin(number)[2:])
#print(number.bit_length())
