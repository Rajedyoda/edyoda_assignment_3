def string_reverse(str1):
    str1 = input("Enter the string to reverse it using function : ")
    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    return rstr1
print(string_reverse('str1'))