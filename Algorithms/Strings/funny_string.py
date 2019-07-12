
CHAR_ARRAY = list(map(chr, range(97, 123)))
STR_HASH = {}
for key, value in enumerate(range(97, 123)):
    STR_HASH[CHAR_ARRAY[key]] = value


def is_funny_string(data_str):
    data_str_list = list(data_str)
    absolute_difference = ordinal_value_of_chars(
        str_list=data_str_list
    )
    reversed_data_str = data_str[::-1]
    reversed_data_str_list = list(reversed_data_str)
    reversed_difference = ordinal_value_of_chars(
        str_list=reversed_data_str_list
    )
    if absolute_difference == reversed_difference:
        return 'Funny'
    else:
        return 'Not Funny'


def ordinal_value_of_chars(str_list):
    value_of_char = []
    for char in str_list:
        value_of_char.append(STR_HASH[char])
    difference = []
    for index in range(len(value_of_char) - 2):
        difference.append(
            abs(value_of_char[index + 1] - value_of_char[index])
        )
    return difference


queries = int(input())
for _ in range(queries):
    string = input()
    print(is_funny_string(data_str=string))
