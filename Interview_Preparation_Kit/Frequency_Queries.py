from collections import Counter
CONST_HASH = {}
FREQ_DICT = Counter()


def freq_query(data):
    if data[0] == 1:
        if CONST_HASH.get(data[1]):
            CONST_HASH[data[1]] += 1
        else:
            CONST_HASH[data[1]] = 1
        FREQ_DICT[CONST_HASH[data[1]]] += 1
        FREQ_DICT[CONST_HASH[data[1]] - 1] -= 1
    elif data[0] == 2:
        if CONST_HASH.get(data[1]):
            FREQ_DICT[CONST_HASH[data[1]]] -= 1
            CONST_HASH[data[1]] -= 1
            FREQ_DICT[CONST_HASH[data[1]]] += 1
    else:
        if FREQ_DICT.get(data[1]):
            print(1)
        else:
            print(0)


queries = int(input())
data = []
for _ in range(queries):
    data.append(list(map(int, input().rstrip().split())))

for _result in data:
    freq_query(data=_result)
