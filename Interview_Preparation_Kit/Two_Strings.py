

def check_common_substring(string1, string2):
    str_dict = dict((key, 1) for key in list(string1))
    for char in list(string2):
        if str_dict.get(char):
            return 'YES'
    return 'NO'


testcases = int(input())
string_pairs = []
for _ in range(testcases):
    string1 = input()
    string2 = input()
    string_pairs.append([string1, string2])

for _data in string_pairs:
    print(check_common_substring(
        string1=_data[0], string2=_data[1]
    ))
