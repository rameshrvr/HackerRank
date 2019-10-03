

def find_counting_sort(N, array):
    middle = (N // 2) - 1
    result = [[] for i in range(100)]
    for index in range(N):
        push_index = int(array[index][0])
        if index <= middle:
            result[push_index].append('-')
        else:
            result[push_index].append(array[index][1])

    result_string = ''
    for data in result:
        if not data == []:
            result_string += ' '.join(data)
            result_string += ' '
    return result_string


###
N = int(input())
array = []
for _ in range(N):
    array.append(input().split())
print(find_counting_sort(N, array))
###
