

def is_valid_string(string):
    # convert the string to char dict
    char_dict = {}
    for char in list(string):
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    result = 0
    mem_value = char_dict[string[0]]
    for unique_char in list(char_dict.keys()):
        if mem_value != char_dict[unique_char]:
            if char_dict[unique_char] == 1:
                result += 1
            else:
                result += abs(mem_value - char_dict[unique_char])
        if result > 1:
            return 'NO'

    return 'YES'


################
string = input()
print(is_valid_string(string))
################
