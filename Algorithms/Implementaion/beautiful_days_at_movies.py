

def find_beautiful_days(start, end, diff):
    beautiful_days = 0
    for day in range(start, end + 1):
        rev_day = reverse_number(number=day)
        if (abs(day - rev_day) % diff) == 0:
            beautiful_days += 1
    return beautiful_days


def reverse_number(number):
    return int(str(number)[::-1])


data = list(map(int, input().split()))
print(find_beautiful_days(start=data[0], end=data[1], diff=data[2]))
