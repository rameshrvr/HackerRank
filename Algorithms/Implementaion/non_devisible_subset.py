

def calc_max_subset_size(array, k):
    """
    Method to calculate the maximum length of the subset
    where sum of any two numbers in the array is not divisible
    by K

    Args:
        array: Array to process
        k: K value
    Return:
        processed array length (Integer)
    """
    # take modulo by k for all elements in the array
    array = [value % k for value in array]
    # Lets assume the subset size is zero initially
    size_of_subset = 0
    # multiple of k can come in the subset only once. So increase the
    # size of the subset by 1 if any multiple of k is there in the subset
    if 0 in array:
        size_of_subset += 1
    # Iterate the loop for (k / 2) times if k=4 then 2 times
    # The Logic behind this is we are counting the values of
    # X and K - X in the Array. Only one from X, K - X can be in subset
    # we will decide which by their count, if X count is more then X
    # will be in the subset and vice versa.
    for x in xrange(1, (k / 2) + 1):
        temp_count1 = array.count(x)
        temp_count2 = array.count(k - x)
        # If K is even in the last iteration of the loop X and K - X
        # will be equal so we can and X only once in the Array.
        if x == (k - x):
            size_of_subset += 1
        else:
            if temp_count1 > temp_count2:
                size_of_subset += temp_count1
            else:
                size_of_subset += temp_count2
    return size_of_subset


############
temp = map(int, raw_input().rstrip().split())
array_size = temp[0]
k = temp[1]
array = map(int, raw_input().rstrip().split())

print calc_max_subset_size(array, k)
############
