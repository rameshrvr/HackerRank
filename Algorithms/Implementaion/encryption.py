import math


def encrypt_the_string(string):
    """
    Method to encrypt the string as per the given problem
    statement

    Args:
            string: String to encrypt
    Return:
            Encrypted string
    """
    string = string.replace(' ', '')
    length = len(string)
    sqrt = math.sqrt(length)
    # calc the row and column value
    if int(sqrt) * (int(sqrt) + 1) < length:
        rows = int(sqrt) + 1
        columns = int(sqrt) + 1
    elif sqrt - int(sqrt) != 0:
        rows = int(sqrt)
        columns = int(sqrt) + 1
    else:
        rows = int(sqrt)
        columns = int(sqrt)
    encrypted_string = []
    for row in xrange(0, columns):
        processed_string = ''
        col = row
        for column in xrange(0, rows):
            if col < length:
                processed_string += string[col]
                col += columns
        encrypted_string.append(processed_string)

    return ' '.join(encrypted_string)


###############
string = raw_input()

print encrypt_the_string(string)
###############
