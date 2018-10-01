
def calc_sequence_equation(array_size, array):
    """
    Method to generate sequence equation of p(p(x))
    where x is an index of an array

    Args:
            array_size: Size of the array
            array: Array of numbers

    Return:
            p(p(x)) value of the array
    """
    result = [0] * array_size
    for index in xrange(0, array_size):
        arr_index = array[(array[index] - 1)]
        result[(arr_index - 1)] = str(index + 1)
    return '\n'.join(result)


########
array_size = int(raw_input())
array = map(int, raw_input().rstrip().split(' '))

print calc_sequence_equation(array_size, array)
########
