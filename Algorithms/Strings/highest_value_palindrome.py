

def highest_value_palindrome(number_string, size, max_changes):
    if size == 1 and max_changes > 0:
        return '9'
    min_changes = 0
    temp_decrease_counter = size - 1
    for index in range(int(size / 2)):
        if number_string[index] != number_string[temp_decrease_counter]:
            min_changes += 1
        if min_changes > max_changes:
            return -1
        temp_decrease_counter -= 1

    bonus_replace_count = max_changes - min_changes
    number_string_list = list(number_string)
    temp_decrease_counter = size - 1
    for index in range(int(size / 2)):
        if bonus_replace_count > 0 and number_string_list[
                index
        ] != '9' and max_changes > 1 and number_string_list[
            temp_decrease_counter
        ] != '9':
            number_string_list[index] = '9'
            number_string_list[temp_decrease_counter] = '9'
            bonus_replace_count -= 1
            max_changes -= 2
        elif number_string_list[index] != number_string_list[
                temp_decrease_counter
        ]:
            if number_string_list[index] > number_string_list[
                    temp_decrease_counter
            ]:
                number_string_list[
                    temp_decrease_counter
                ] = number_string_list[index]
            else:
                number_string_list[index] = number_string_list[
                    temp_decrease_counter
                ]
            max_changes -= 1
        temp_decrease_counter -= 1
        if max_changes == 0:
            break
    if max_changes > 0 and size % 2 == 1:
        number_string_list[int(size / 2)] = '9'
    return ''.join(number_string_list)


details = list(map(int, input().split()))
string_size, max_changes = details[0], details[1]
number_string = input()

print(
    highest_value_palindrome(
        number_string=number_string, size=string_size,
        max_changes=max_changes
    )
)
