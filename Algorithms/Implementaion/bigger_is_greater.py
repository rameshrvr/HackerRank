

def get_first_lexicographical_larger_string(string):
    str_list = list(string)
    str_size = len(str_list)
    sub_str_size = 1
    for index in range(str_size - 1, int((str_size - 1) / 2), -1):
        if string[index:] > string[index - sub_str_size:index]:
            str_list[index:], str_list[
                (index - sub_str_size):index
            ] = str_list[(index - sub_str_size):index], str_list[index:]
            break
        sub_str_size += 1
    else:
        return 'no answer'
    return ''.join(str_list)


test_cases = int(input())

for _ in range(test_cases):
    string = input()
    print(get_first_lexicographical_larger_string(string=string))
