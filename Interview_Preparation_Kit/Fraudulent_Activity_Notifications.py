import bisect


def calc_fraud_activity(array, d, size):
    result = 0
    # Initialize the sub array with original array
    # index starting from 0 to d - 1
    sub_array = array[:d]
    # Sort the sub array O(N * log N)
    # (Note: we are going to sort the array only once)
    sub_array.sort()
    median = get_median(sub_array=sub_array, d=d)
    if array[d] >= (2 * median):
        result += 1

    # The idea is to re-form the sorted array by deleting an
    # element from it and inserting another element without
    # disturbing the sorted property of the array
    start_index = 0
    for index in range(d + 1, size):
        # Find the deletable index
        deletable_index = binary_search(
            array=sub_array, element=array[start_index],
            left=0, right=(d - 1)
        )
        # Delete the element from sub array
        del sub_array[deletable_index]
        # Insert the element to sub array and make sure it is in sorted
        # order
        bisect.insort(sub_array, array[index - 1])
        # Find median of the sub array and calc result.
        median = get_median(sub_array=sub_array, d=d)
        if array[index] >= (2 * median):
            result += 1
        start_index += 1
    return result


def get_median(sub_array, d):
    if d % 2 == 0:
        return (sub_array[(d // 2)] + sub_array[(d // 2) - 1]) / 2
    else:
        return sub_array[(d // 2)]


def binary_search(array, element, left, right):
    middle = (left + right) // 2
    if array[middle] == element:
        return middle
    elif array[middle] > element:
        return binary_search(
            array=array, element=element, left=left, right=(middle - 1)
        )
    else:
        return binary_search(
            array=array, element=element, left=(middle + 1), right=right
        )


if __name__ == "__main__":
    data = list(map(int, input().split()))
    array = list(map(int, input().split()))

    print(
        calc_fraud_activity(array=array, d=data[1], size=data[0])
    )
