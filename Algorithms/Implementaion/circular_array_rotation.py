

def do_circular_array_rotation(size_of_array, array, no_of_rotation):
    """
    Method to do circular array rotation as per the given
    number of rotations

    Args:
            array: Array of numbers
            no_of_rotation: No of Rotations to perform

    Return:
            Array after rotation
    """
    min_rotation = no_of_rotation % size_of_array
    min_rotation = -1 * min_rotation
    return array[min_rotation:] + array[:min_rotation]


#############
test_case_details = map(int, raw_input().rstrip().split())
array = map(int, raw_input().rstrip().split())
elements_to_print = []
for _ in xrange(0, test_case_details[2]):
    elements_to_print.append(int(raw_input()))

result = do_circular_array_rotation(
    size_of_array=test_case_details[0], array=array,
    no_of_rotation=test_case_details[1]
)

for index in elements_to_print:
    print result[index]
#############
