

def ice_cream_parlor(total_amount, data):
    DATA_HASH = {}
    for key, value in enumerate(data):
        if value in DATA_HASH:
            temp = DATA_HASH[value]
            DATA_HASH[value] = [temp, key + 1]
        else:
            DATA_HASH[value] = key + 1
    # generate possible combinations
    for start in range(1, int(total_amount / 2) + 1):
        end = total_amount - start
        if start in DATA_HASH and end in DATA_HASH:
            if isinstance(DATA_HASH[start], list):
                result = []
                if DATA_HASH[start][0] > DATA_HASH[start][1]:
                    result = [DATA_HASH[start][1], DATA_HASH[start][0]]
                else:
                    result = [DATA_HASH[start][0], DATA_HASH[start][1]]
                return "{} {}".format(result[0], result[1])
            result = []
            if DATA_HASH[start] > DATA_HASH[end]:
                result = [DATA_HASH[end], DATA_HASH[start]]
            else:
                result = [DATA_HASH[start], DATA_HASH[end]]
            return "{} {}".format(result[0], result[1])


test_cases = int(input())

for _ in range(test_cases):
    total_amount = int(input())
    data_size = int(input())
    data = list(map(int, input().split()))
    print(ice_cream_parlor(total_amount=total_amount, data=data))
