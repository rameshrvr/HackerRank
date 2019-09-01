

def get_special_string_count(string, size):
    char_array = list(string)
    temp_count = 1
    cursor = char_array[0]
    data = []
    for index in range(1, size):
        if char_array[index] == cursor:
            temp_count += 1
        else:
            data.append([cursor, temp_count])
            cursor = char_array[index]
            temp_count = 1
    data.append([cursor, temp_count])
    result = 0
    for _ind_data in data:
        result += (_ind_data[1] * (_ind_data[1] + 1)) // 2

    for index in range(1, len(data) - 1):
        if data[index - 1][0] == data[index + 1][0] and data[index][1] == 1:
            result += min(data[index - 1][1], data[index + 1][1])
    return result


################
size = int(input())
string = input()
print(get_special_string_count(string=string, size=size))
################
