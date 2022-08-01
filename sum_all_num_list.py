def sum_list(num):
    sum_off = 0
    for i in num:
        sum_off += i
    return sum_off
print("Sum of all the numbers in a list is: ",sum_list((8, 2, 3, 0, 7)))