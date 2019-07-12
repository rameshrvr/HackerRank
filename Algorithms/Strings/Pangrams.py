

def pangrams_or_not(data_string):
    data_string = data_string.replace(' ', '')
    char_hash = {}
    for char in list(data_string):
        char = char.lower()
        if char in char_hash:
            char_hash[str(char)] += 1
        else:
            char_hash[str(char)] = 1
    if len(char_hash.keys()) == 26:
        return 'pangram'
    else:
        return 'not pangram'


string = input()
print(pangrams_or_not(data_string=string))
