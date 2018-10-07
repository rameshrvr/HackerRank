
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


def disp_app_names(n, strings):
    display = []
    display.append(strings[0][0])
    for index1 in xrange(1, n):
        for index2 in list(reversed(xrange(0, index1))):
            if strings.count(strings[index1]) > 1:
                count = strings[:index2].count(strings[index1])
                if count == 0:
                    matching_substr = get_matching_substring(
                        strings[index1], strings[index2])
                    if matching_substr != '':
                        length = len(matching_substr)
                        disp_name = strings[index1][:(length + 1)]
                        display.append(disp_name)
                        break
                display.append('{} {}'.format(strings[index1], count + 1))
                break
            matching_substr = get_matching_substring(
                strings[index1], strings[index2])
            if matching_substr != '':
                length = len(matching_substr)
                disp_name = strings[index1][:(length + 1)]
                display.append(disp_name)
                break
            if index2 == 0 and matching_substr == '':
                display.append(strings[index1][0])
    return '\n'.join(display)


########
n = int(raw_input())
strings = []
for _ in xrange(0, n):
    strings.append(raw_input().rstrip())

print disp_app_names(n, strings)
########
