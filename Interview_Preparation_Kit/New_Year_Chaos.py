

def get_minimum_bribes(array, length):
    result = 0
    swaped = False
    for index in range(length - 1):
        if array[index] - (index + 1) > 2:
            return 'Too chaotic'
    for _ in range(length):
        for index in range(length - 1):
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]
                result += 1
                swaped = True
        if swaped:
            swaped = False
        else:
            break
    return result


test_cases = int(input())
data_size = []
data = []
for _ in range(test_cases):
    data_size.append(int(input()))
    data.append(list(map(int, input().rstrip().split(' '))))

for index in range(test_cases):
    print(get_minimum_bribes(array=data[index], length=data_size[index]))
