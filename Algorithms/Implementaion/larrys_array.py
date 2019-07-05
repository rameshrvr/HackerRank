
def larrys_array(data_size, data):
    index_hash = {}
    value_hash = {}
    for key, value in enumerate(data):
        value_hash[value] = key + 1
        index_hash[key + 1] = value

    for _count in range(1, data_size - 1):
        if value_hash[_count] == _count:
            continue
        if value_hash[_count] - _count > 1:
            while (value_hash[_count] - _count) >= 2:
                double_roatation(
                    hash1=index_hash, hash2=value_hash,
                    start=get_swapable_start(
                        start=_count, value_hash=value_hash
                    )
                )
            if (value_hash[_count] - _count) == 1:
                single_roatation(
                    hash1=index_hash, hash2=value_hash,
                    start=get_swapable_start(
                        start=_count, value_hash=value_hash
                    )
                )
        else:
            single_roatation(
                hash1=index_hash, hash2=value_hash,
                start=get_swapable_start(
                    start=_count, value_hash=value_hash
                )
            )
    if value_hash[data_size - 1] == (data_size - 1):
        return 'YES'
    else:
        return 'NO'


def double_roatation(hash1, hash2, start):
    temp1 = hash1[start]
    temp2 = hash1[start + 1]
    temp3 = hash1[start + 2]
    # Replace hash2
    hash2[temp1] += 1
    hash2[temp2] += 1
    hash2[temp3] -= 2
    # Replace hash1
    hash1[hash2[temp1]] = temp1
    hash1[hash2[temp2]] = temp2
    hash1[hash2[temp3]] = temp3


def single_roatation(hash1, hash2, start):
    temp1 = hash1[start]
    temp2 = hash1[start + 1]
    temp3 = hash1[start + 2]
    # Replace hash2
    hash2[temp1] += 2
    hash2[temp2] -= 1
    hash2[temp3] -= 1
    # Replace hash1
    hash1[hash2[temp1]] = temp1
    hash1[hash2[temp2]] = temp2
    hash1[hash2[temp3]] = temp3


def get_swapable_start(start, value_hash):
    temp = value_hash[start] - start
    if temp >= 2:
        return value_hash[start] - 2
    else:
        return value_hash[start] - 1


test_cases = int(input())
for _ in range(test_cases):
    arr_size = int(input())
    data = list(map(int, input().split(' ')))
    data_hash = {value: key + 1 for key, value in enumerate(data)}
    data_pass = []
    for _check in sorted(data):
        data_pass.append(data_hash[_check])
    print(larrys_array(data_size=arr_size, data=data_pass))
