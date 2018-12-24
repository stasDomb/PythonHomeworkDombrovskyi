
number = 15

binary_view = str(bin(number)[2:])
print(binary_view)
max_gap_length = 0
cur_gap_length = 0
for i in range(len(binary_view)):
    # if number & (1 << i):
    if binary_view[i] == "0":
        print("digit = 0")
        # Not set, the gap widens.
        cur_gap_length += 1

    else:
        # Set, any gap is over

        print("digit = 1")
        if cur_gap_length > max_gap_length:
            max_gap_length = cur_gap_length
        cur_gap_length = 0

print(max_gap_length)
