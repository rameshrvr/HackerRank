

def calc_fraud_activity(array, d):
    result = 0
    for i in range(d, len(array)):
        median = get_median(
            sub_array=array[i - d:i - 1], d=d
        )
        if array[i] >= (2 * median):
            result += 1
    return result


def get_median(sub_array, d):
    sub_array.sort()
    if d % 2 == 0:
        return (sub_array[(d // 2)] + sub_array[(d // 2) - 1]) / 2
    else:
        return sub_array[(d // 2)]


data = list(map(int, input().rstrip().split()))
array = list(map(int, input().rstrip().split()))

print(
    calc_fraud_activity(array=array, d=data[1])
)
