

def calc_beautiful_triplets(array, diff):
    """
    Method to calculate beautiful triplet count
    Args:
        array: Array of numbers
        diff: Beautiful triplet difference between each element
    Return:
        count of beautiful triplets
    """
    result = 0
    for number in array:
        if (number + diff) in array and (number + 2 * diff) in array:
            result += 1
    return result


###################
prob_details = map(int, raw_input().strip().split())
my_array = map(int, raw_input().strip().split())

print calc_beautiful_triplets(array=my_array, diff=prob_details[1])
###################
