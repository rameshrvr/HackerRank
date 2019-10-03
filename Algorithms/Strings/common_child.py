

def longest_common_string(string1, string2):
    str1_dict = {}
    str2_dict = {}
    for index, char in enumerate(list(string1)):
        if char in str1_dict:
            str1_dict[char].append(index)
        else:
            str1_dict[char] = [index]

    for index, char in enumerate(list(string2)):
        if char in str2_dict:
            str2_dict[char].append(index)
        else:
            str2_dict[char] = [index]

    cons_index = -1
    result = 0
    for char in list(string1):
        if char in str2_dict:
            for data in str2_dict[char]:
                if data > cons_index:
                    result += 1
                    cons_index = data
                    break

    return result


###
string1 = input()
string2 = input()
print(longest_common_string(string1, string2))
###
