

def solve_problem(array, size):
    min_number = float('inf')
    trace_dict = {}
    # Find maximum and minimum numbers in array
    for number in array:
        if number in trace_dict:
            trace_dict[number] += 1
        else:
            trace_dict[number] = 1
        if number < min_number:
            min_number = number

    result_sum1 = 0
    result_sum2 = 0
    for number in trace_dict.keys():
        if not number == min_number:
            result_sum1 += get_multiplier_count(
                num=number, min_number=min_number
            ) * trace_dict[number]
        result_sum2 += get_multiplier_count(
            num=number, min_number=0
        ) * trace_dict[number]

    return min(result_sum1, result_sum2)


def get_multiplier_count(num, min_number):
    difference = num - min_number
    result = 0
    for iter_num in [5, 2, 1]:
        if difference >= iter_num:
            result += int(difference / iter_num)
            if difference % iter_num == 0:
                break
            difference = difference % iter_num

    return result


###################
testcases = int(input())
for _ in range(testcases):
    size = int(input())
    array = list(map(int, input().split()))
    print(solve_problem(array=array, size=size))
###################
