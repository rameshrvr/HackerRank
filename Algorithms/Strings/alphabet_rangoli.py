import string

l_chars = list(string.ascii_lowercase)


def alphabet_rangoli(size):
    coulmn_size = (size + (size - 1)) + (size + (size - 2))
    alpha_array = list(reversed(l_chars[:size]))
    rangoli_list = []
    for number in range(size):
        _size = (coulmn_size - ((number * 4) + 1)) // 2
        char_list = alpha_array[:(number + 1)]
        processed_char_list = char_list + list(reversed(char_list))[1:]
        rangoli_list.append(
            '{0}{1}{0}'.format(
                '-' * _size, '-'.join(processed_char_list)
            )
        )
    for index in reversed(range(size - 1)):
        rangoli_list.append(rangoli_list[index])
    return rangoli_list


def get_alphabet_design(start_index):
    return


####
size = int(input())
rangoli_list = alphabet_rangoli(size)
for data in rangoli_list:
    print(data)
####
