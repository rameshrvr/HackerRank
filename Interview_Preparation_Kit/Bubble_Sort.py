

def count_swaps(array, size):
    swaps = 0
    for i in range(size):
        for j in range(size - 1):
            if array[j] > array[j + 1]:
                swaps += 1
                array[j], array[j + 1] = array[j + 1], array[j]
    print('Array is sorted in {} swaps.'.format(swaps))
    print('First Element: {}'.format(array[0]))
    print('Last Element: {}'.format(array[size - 1]))


size = int(input())
array = list(map(int, input().rstrip().split()))

count_swaps(array=array, size=size)
