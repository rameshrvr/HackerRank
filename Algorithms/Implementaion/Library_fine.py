

def LibraryFine(expected_date, actual_date):
    """
            Method to calculate the fine amount

            @param expected_date: expected date of submission
            @param actual_date: Actual date of submission

            @return Fine
    """
    if not expected_date[2] == actual_date[2]:
        if expected_date[2] > actual_date[2]:
            return 0
        else:
            return 10000
    elif expected_date[1] == actual_date[1]:
        if actual_date[0] <= expected_date[0]:
            return 0
        else:
            return (actual_date[0] - expected_date[0]) * 15
    elif expected_date[1] <= actual_date[1]:
        return (actual_date[1] - expected_date[1]) * 500
    else:
        return 0


actual_date = map((lambda x: int(x)), (raw_input().split()))
expected_date = map((lambda x: int(x)), (raw_input().split()))

print LibraryFine(expected_date, actual_date)
