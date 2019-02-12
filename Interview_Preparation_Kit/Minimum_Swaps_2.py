
def find_minimum_swaps(size, array):
    mapped_array = list(enumerate(array))
    # Map sorted array with its unsorted index
    mapped_array.sort(key=lambda x: x[1])
    # Declare memory array
    memory = [0] * size
    result = 0
    for index in range(size):
        if memory[index] or (mapped_array[index][0] == index):
            continue
        swaps = 0
        temp = index
        while not memory[temp]:
            # Set memory
            memory[temp] = 1
            temp = mapped_array[temp][0]
            swaps += 1
        if swaps > 0:
            result += (swaps - 1)
    return result


arr_size = int(input())
array = list(map(int, input().rstrip().split(' ')))

print(find_minimum_swaps(size=arr_size, array=array))
