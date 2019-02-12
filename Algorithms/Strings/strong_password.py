

def get_minimum_char_for_strong_password(password, length):
    numbers = list("0123456789")
    lower_case = list("abcdefghijklmnopqrstuvwxyz")
    upper_case = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    special_characters = list("!@#$%^&*()-+")

    char_array = list(password)
    temp = [0] * 4
    for char in char_array:
        if char in numbers:
            temp[0] = 1
        if char in lower_case:
            temp[1] = 1
        if char in upper_case:
            temp[2] = 1
        if char in special_characters:
            temp[3] = 1

    result = (4 - sum(temp))
    if length + result >= 6:
        return result
    else:
        return result + (6 - length - result)


str_len = int(input())
password = input()

print(get_minimum_char_for_strong_password(
    password=password, length=str_len
))
