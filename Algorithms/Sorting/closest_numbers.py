

def find_closest_numbers(data_set):
    closest_numbers = []
    closest_diff = abs(data_set[0] - data_set[1])
    for index in range(1, len(data_set) - 1):
        diff = abs(data_set[index] - data_set[index + 1])
        if diff < closest_diff:
            closest_diff = diff
            closest_numbers = []
            closest_numbers = [str(data_set[index]), str(data_set[index + 1])]
        elif diff == closest_diff:
            closest_numbers.extend(
                [str(data_set[index]), str(data_set[index + 1])]
            )
    return ' '.join(closest_numbers)


arr_size = int(input())
data = list(map(int, input().split()))

data.sort()

print(find_closest_numbers(data_set=data))
