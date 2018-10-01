import math


def calc_square_integers(start_range, end_range):
    """
    Method to calculate the square integers between the given
    start and end range

    Args:
            start_range: Start range
            end_range: End range
    Return:
            Number of square integers(Integer)
    """
    start_num = int(math.sqrt(start_range))
    result = 1 if calc_square(start_num) == start_range else 0
    start_num += 1
    while True:
        if calc_square(start_num) <= end_range:
            result += 1
        else:
            break
        start_num += 1
    return result


def calc_square(number):
    """
    Method to calculate square
    """
    return number**2


###########
test_cases = int(raw_input())
number_range = []
for _ in xrange(0, test_cases):
    number_range.append(map(int, raw_input().rstrip().split()))

for index in xrange(0, test_cases):
    print calc_square_integers(
        start_range=number_range[index][0],
        end_range=number_range[index][1]
    )
###########
