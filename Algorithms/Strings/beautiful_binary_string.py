

def beautiful_binary_string(binary_string, size):
    result = 0
    start = 0
    str_list = list(binary_string)
    while start < (size - 2):
        if str_list[start] == str_list[start + 2] == '0' and str_list[start + 1] == '1':
            result += 1
            start += 2
        start += 1
    return result


####
size = int(input())
binary_string = input()
print(beautiful_binary_string(binary_string, size))
####
