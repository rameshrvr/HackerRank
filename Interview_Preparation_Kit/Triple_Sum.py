import collections

IJ_INDEX = [0]


def binary_search(start, end, element, data):
    middle = (start + end) // 2
    if data[middle] == element:
        return middle
    if data[IJ_INDEX[0]] < data[middle] < element:
        IJ_INDEX[0] = middle

    if start == end or end < start:
        return False

    if data[middle] > element:
        return binary_search(
            start=start, end=(middle - 1), element=element, data=data
        )
    else:
        return binary_search(
            start=(middle + 1), end=end, element=element, data=data
        )


def calc_triple_sum(data1, data2, data3):
    result = 0
    size1 = len(data1)
    size3 = len(data3)
    for ind_data in data2:
        mul1 = 0
        mul2 = 0
        ###
        IJ_INDEX[0] = 0
        ###
        temp1 = binary_search(start=0, end=(size1 - 1),
                              element=ind_data, data=data1)
        if temp1 is False:
            if IJ_INDEX[0] == 0 and data1[0] > ind_data:
                mul1 = 0
            else:
                mul1 = IJ_INDEX[0] + 1
        else:
            mul1 = temp1 + 1
        ###
        IJ_INDEX[0] = 0
        ###
        temp2 = binary_search(start=0, end=(size3 - 1),
                              element=ind_data, data=data3)
        if temp2 is False:
            if IJ_INDEX[0] == 0 and data3[0] > ind_data:
                mul2 = 0
            else:
                mul2 = IJ_INDEX[0] + 1
        else:
            mul2 = temp2 + 1
        result += (mul1 * mul2)
    return result


##########
size_array = list(map(int, input().split()))
data1 = list(collections.OrderedDict.fromkeys(
    list(map(int, input().split()))))
data2 = list(collections.OrderedDict.fromkeys(list(map(int, input().split()))))
data3 = list(collections.OrderedDict.fromkeys(
    list(map(int, input().split()))))
data1 = list(sorted(data1))
data3 = list(sorted(data3))
print(calc_triple_sum(data1, data2, data3))
##########
