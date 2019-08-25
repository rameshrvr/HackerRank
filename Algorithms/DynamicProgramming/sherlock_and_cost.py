

def calc_max_cost(array, size):
    t1 = 0
    t2 = 0
    for index in range(size - 1):
        diff1 = abs(array[index + 1] - 1)
        diff2 = abs(1 - array[index])
        temp = t1
        t1 = t2 + diff1
        t2 = temp + diff2

    return max(t1, t2)


########################
testcases = int(input())
for _ in range(testcases):
    array_size = int(input())
    array = list(map(int, input().split()))
    print(calc_max_cost(array=array, size=array_size))
########################
