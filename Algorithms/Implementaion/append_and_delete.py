

def get_matching_substring(string1, string2):
    """
    Method to get the matching substring from the two given string

    Args:
        string1: string1
        string2: string2
    Return:
        Matching sub string
    """
    matching_string = []
    for a, b in zip(string1, string2):
        if a == b:
            matching_string.append(a)
        else:
            break
    return ''.join(matching_string)


def determine_append_delete_is_possible(string1, string2, operations):
    """
    Method to determine append delete in a string is possible
    for the given number of operations (After all operations both
    strings should be equal)

    Args:
        string1: string1
        string2: string2
        operations: No of operations to perform
    Return:
        Bool - 'Yes'/'No'
    """
    matching_string = get_matching_substring(string1, string2)
    string1_len = len(string1) - len(matching_string)
    string2_len = len(string2) - len(matching_string)
    if string1_len == 0 and string2_len != 0:
        if (operations - string2_len) % 2 != 0:
            return 'No'
    if (string1_len + string2_len) == operations \
            or (string1_len + string2_len + 2) <= operations:
        return 'Yes'
    else:
        return 'No'


##########
string1 = input()
string2 = input()
operations = int(input())

print(determine_append_delete_is_possible(string1, string2, operations))
##########
