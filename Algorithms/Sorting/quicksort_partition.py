

def get_partitioned_array(array):
    pivot = array[0]
    array = array[1:]
    before_pivot = []
    after_pivot = []
    for data in array:
        if data > pivot:
            after_pivot.append(data)
        else:
            before_pivot.append(data)
    result_list = before_pivot + [pivot] + after_pivot
    result_list = [str(i) for i in result_list]
    return ' '.join(result_list)


arr_size = int(input())
array = list(map(int, input().split()))

print(get_partitioned_array(array=array))
