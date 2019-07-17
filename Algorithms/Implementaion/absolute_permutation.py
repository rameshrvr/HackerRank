

def calc_absolute_permutation(data):
    result_range = [value + 1 for value in range(data[0])]
    k_value = data[1]
    if k_value == 0:
        return ' '.join(list(map(str, result_range)))
    if data[0] % (k_value + k_value) != 0:
        return -1
    temp_counter = 0
    for _ in range(int(data[0] / (2 * k_value))):
        for index in range(k_value):
            swap1_index = index + temp_counter
            swap2_index = swap1_index + k_value
            result_range[swap1_index], result_range[
                swap2_index
            ] = result_range[swap2_index], result_range[swap1_index]
        temp_counter += (2 * k_value)
    return ' '.join(list(map(str, result_range)))


####################
test_cases = int(input())
for _ in range(test_cases):
    data = list(map(int, input().split()))
    print(calc_absolute_permutation(data=data))
####################
