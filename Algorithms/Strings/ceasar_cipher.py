

def cipher_string(string, rotation, length):
    string = list(string)
    rotation = rotation % 26
    for index in range(length):
        ascii_value = ord(string[index])
        if 64 < ascii_value < 91:
            new_ascii = ascii_value + rotation
            if new_ascii > 90:
                new_ascii -= 26
            string[index] = chr(new_ascii)
        elif 96 < ascii_value < 123:
            new_ascii = ascii_value + rotation
            if new_ascii > 122:
                new_ascii -= 26
            string[index] = chr(new_ascii)

    return ''.join(string)


length = int(input())
string = input()
rotation = int(input())

print(cipher_string(
    string=string, length=length, rotation=rotation
))
