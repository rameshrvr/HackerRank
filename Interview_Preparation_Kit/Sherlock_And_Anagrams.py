import math
from collections import defaultdict


def find_substring_anagram_count(string):
    result = 0
    SUB_STR_HASH = {}
    COUNT_CONST = defaultdict(list)
    length = len(string)
    for i in range(length):
        for j in range(i, length):
            if SUB_STR_HASH.get(string[i:j + 1]):
                SUB_STR_HASH[string[i:j + 1]] += 1
            else:
                SUB_STR_HASH[string[i:j + 1]] = 1
    for key in SUB_STR_HASH:
        if SUB_STR_HASH[key] > 1:
            result += nCr(n=SUB_STR_HASH[key], r=2)
        length = len(key)
        COUNT_CONST[length].append(key)
    for key, value in COUNT_CONST.items():
        if key != 1:
            for temp1 in value:
                for temp2 in value:
                    if temp1 != temp2:
                        if sorted(temp1) == sorted(temp2):
                            result += (
                                SUB_STR_HASH[temp1] * SUB_STR_HASH[temp2]
                            )
                SUB_STR_HASH[temp1] = 0
    return result


def nCr(n, r):
    f = math.factorial
    return f(n) // f(r) // f(n - r)


queries = int(input())
data = []
for _ in range(queries):
    data.append(input().rstrip())


for string in data:
    print(find_substring_anagram_count(string=string))
