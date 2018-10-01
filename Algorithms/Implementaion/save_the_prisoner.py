

def calc_prisioner_seat_number(
        no_of_prisoners, no_of_sweets, chair_to_start
):
    """
    Method to calculate prisoner seat number whom to be
    warned while receiving the candy

    Args:
        no_of_prisoners: number of prisoners
        no_of_sweets: number of sweets
        chair_to_start: chair number to start passing out treats at

    Return:
        chair number of the prisoner who receives the awful treat
        (Integer)
    """
    result = (no_of_sweets + (chair_to_start - 1)) % no_of_prisoners
    return no_of_prisoners if result == 0 else result


############
test_cases = int(raw_input())
test_case_details = []
for _ in xrange(0, test_cases):
    test_case_details.append(map(int, raw_input().rstrip().split()))

for test_case in test_case_details:
    print calc_prisioner_seat_number(
        no_of_prisoners=test_case[0], no_of_sweets=test_case[1],
        chair_to_start=test_case[2]
    )
############
