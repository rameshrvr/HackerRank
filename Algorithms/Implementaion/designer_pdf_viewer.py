

def calc_highlighted_area(array, string_array):
    alphabet_array = []
    for i in range(97, 124):
        alphabet_array.append(chr(i))
    my_dict = dict(zip(alphabet_array, array))
    max_hight = 0
    width = len(string_array)
    for char in string_array:
        if my_dict[char] >= max_hight:
            max_hight = my_dict[char]

    return max_hight * width


########
array = map(int, raw_input().rstrip().split(' '))
string_array = str(raw_input())

print calc_highlighted_area(array, list(string_array))
########
