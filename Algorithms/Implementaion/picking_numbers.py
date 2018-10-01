
def calc_max_length_of_sub_array(array):
    """
    Method to calculate the max length of sub array
    where the absolute difference between any 2 elements
    in the array is 1

    Args:
            array: Input Array

    Returns:
            Max length of the sub array (Integer)
    """
    result = []
    another_result = []
    sorted_array = sorted(set(array))
    size = len(sorted_array)
    if size == 1:
        return array.count(sorted_array[0])
    for index in xrange(0, size - 1):
        if abs(sorted_array[index] - sorted_array[index + 1]) == 1:
            result.append(
                array.count(
                    sorted_array[index]
                ) + array.count(
                    sorted_array[index + 1]
                )
            )
        else:
            another_result.append(
                array.count(sorted_array[index])
            )
    if another_result and max(another_result) > max(result):
        return max(another_result)
    return max(result) if result else max(another_result)


###########
array_size = int(raw_input())
array = map(int, raw_input().rstrip().split(' '))

print calc_max_length_of_sub_array(array)
###########
