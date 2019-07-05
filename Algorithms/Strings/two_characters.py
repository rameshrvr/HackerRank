

def get_unique_char_list(char_array):
    unique_str_hash = {}
    for char in char_array:
        if char in unique_str_hash:
            unique_str_hash[char] += 1
        else:
            unique_str_hash[char] = 1

    return list(unique_str_hash.keys())


def get_answer_string_size(char_array):
    unique_char_list = get_unique_char_list(
        char_array=char_array
    )
    answer_string_size = []
    for i in range(len(unique_char_list) - 1):
        for j in range(i + 1, len(unique_char_list)):
            answer_string_size.append(
                get_modified_str_length(
                    char1=unique_char_list[i],
                    char2=unique_char_list[j],
                    array=char_array, char_list=unique_char_list
                )
            )
    if answer_string_size == []:
        return 0
    return max(answer_string_size)


def get_modified_str_length(char1, char2, array, char_list):
    processed_str = ''.join(array)
    for char in char_list:
        if char == char1 or char == char2:
            continue
        else:
            processed_str = processed_str.replace(char, '')
    processed_str = list(processed_str)
    for index in range(len(processed_str) - 1):
        if processed_str[index] == processed_str[index + 1]:
            return 0
    else:
        return len(processed_str)


string_len = int(input())
char_array = list(input().strip())
print(get_answer_string_size(char_array=char_array))
