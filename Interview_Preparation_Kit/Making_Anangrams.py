

def find_no_of_deletions(string1, string2):
    char_hash1 = {}
    char_hash2 = {}
    for char in list(string1):
        if char in char_hash1:
            char_hash1[char] += 1
        else:
            char_hash1[char] = 1

    for char in list(string2):
        if char in char_hash2:
            char_hash2[char] += 1
        else:
            char_hash2[char] = 1

    result = 0
    for uniq_char in list(char_hash1.keys()):
        if uniq_char in char_hash2:
            diff = abs(char_hash1[uniq_char] - char_hash2[uniq_char])
            result += diff
            char_hash1.pop(uniq_char, None)
            char_hash2.pop(uniq_char, None)

    for remaining_char in list(char_hash1.keys()):
        result += char_hash1[remaining_char]

    for remaining_char in list(char_hash2.keys()):
        result += char_hash2[remaining_char]

    return result


####################
string1 = input()
string2 = input()
print(find_no_of_deletions(string1, string2))
####################
