

def check_is_beautiful(data_str):
    if data_str[0] == '0':
        return 'NO'
    start_index = find_digit_size(string_array=list(data_str))
    if start_index == 0:
        return 'NO'
    start = 0
    end = start_index
    digit_size = start_index
    while start < len(data_str) - 1:
        integet_set = list(set(data_str[start:end]))
        if len(integet_set) == 1 and integet_set[0] == '9':
            digit_size += 1
        if end + start_index > len(data_str):
            break
        if not int(data_str[start:end]) + 1 == int(
                data_str[end:(end + digit_size)]
        ):
            return 'NO'
        start = end
        end += digit_size
    return 'YES {}'.format(data_str[:start_index])


def find_digit_size(string_array):
    digit_size = 1
    index = 1
    while index <= (len(string_array) / 2):
        integet_set = list(set(data_str[:digit_size]))
        if len(integet_set) == 1 and integet_set[0] == '9':
            digit_size += 1
        if int(data_str[:index]) + 1 == int(
                data_str[index:(index + digit_size)]
        ):
            search_index = 2 if data_str[index] == '9' else 1
            if digit_size == 1:
                if int(data_str[index:index + 1]) + 1 == int(
                        data_str[index + 1:(index + 1 + search_index)]
                ):
                    return index
            else:
                return index
        index += 1
        digit_size = index
    return 0


queries = int(input())

for _ in range(queries):
    data_str = input()
    print(check_is_beautiful(data_str=data_str))
