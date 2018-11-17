

def modified_kaprekar_numbers(start_range, end_range):
    """
    Method to find all possible karprekar number between the
    given range of numbers

    Args:
        start_range: Start range
        end_range: End range
    Return:
        karprekar numbers or 'INVALID RANGE'
    """
    karprekar_number = []
    for number in xrange(start_range, end_range + 1):
        square = number ** 2
        split = split_number(number=square)
        if split[0] + split[1] == number:
            karprekar_number.append(str(number))
    if karprekar_number:
        return ' '.join(karprekar_number)
    else:
        return 'INVALID RANGE'


def split_number(number):
    """
    Method to split the number into 2 parts
    Ex: '45' => '4', '5'

    Args:
        number: Number to split
    Return:
        Array of splited number
    """
    length = len(str(number)) / 2
    start = str(number)[:length] if str(number)[:length] != '' else 0
    end = str(number)[length:]
    return [int(start), int(end)]


#############
start_range = int(raw_input())
end_range = int(raw_input())

print modified_kaprekar_numbers(start_range, end_range)
#############
