

def get_fair_rations(array, arr_size):
    index = 0
    minimum_distribution = 0
    while True:
        if index == arr_size - 1:
            break
        if (array[index] % 2) == 0:
            index += 1
        elif (array[index] % 2) == 1:
            minimum_distribution += 2
            array[index] += 1
            array[index + 1] += 1
        else:
            break
    if (array[arr_size - 1] % 2) == 1:
        return 'NO'
    return minimum_distribution


my_input = int(raw_input())
array = map(int, raw_input().rstrip().split(' '))

print get_fair_rations(
    array=array, arr_size=my_input
)
