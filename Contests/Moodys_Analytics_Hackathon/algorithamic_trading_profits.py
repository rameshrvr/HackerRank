
def solve(profits, w):
    """
    """
    max_profit = [0] * 4
    max_array = find_max_array(profits)
    maximum = max(max_array)
    index_arr = max_array.index(maximum)
    # index_of_max_profit_array = profits[index_arr].index(maximum)
    if index_arr == (w - 1):
        for index_of_max_profit_array in xrange(0, w):
            max_profit[index_of_max_profit_array] += maximum
            two_value_arr = []
            two_value_arr.append(index_of_max_profit_array)
            index_arr -= 1
            while index_arr >= 0:
                find_index = find_max_without_dup(
                    profits[index_arr], two_value_arr
                )
                if len(two_value_arr) == 2:
                    two_value_arr[0] = two_value_arr[1]
                    two_value_arr[1] = find_index
                else:
                    two_value_arr.append(find_index)
                max_profit[index_of_max_profit_array] += profits[index_arr][find_index]
                index_arr -= 1
    elif index_arr == 0:
        for index_of_max_profit_array in xrange(0, w):
            max_profit[index_of_max_profit_array] += maximum
            two_value_arr = []
            two_value_arr.append(index_of_max_profit_array)
            index_arr += 1
            while index_arr < w:
                find_index = find_max_without_dup(
                    profits[index_arr], two_value_arr
                )
                if len(two_value_arr) == 2:
                    two_value_arr[0] = two_value_arr[1]
                    two_value_arr[1] = find_index
                else:
                    two_value_arr.append(find_index)
                max_profit[index_of_max_profit_array] += profits[index_arr][find_index]
                index_arr += 1

    return max(max_profit)


def find_max_without_dup(array, not_in_arr):
    """
    """
    maximum = max(array)
    index_of_max = array.index(maximum)
    if index_of_max in not_in_arr:
        array[index_of_max] = 0
        return find_max_without_dup(array, not_in_arr)
    else:
        return index_of_max


def find_max_array(profits):
    """
    """
    max_array = []
    for inner_array in profits:
        max_array.append(max(inner_array))
    return max_array


#############
q = int(raw_input().strip())

for q_itr in xrange(q):
    w = int(raw_input().strip())
    profits = []
    for _ in xrange(w):
        profits.append(map(int, raw_input().rstrip().split()))
    print solve(profits, w)
#############
