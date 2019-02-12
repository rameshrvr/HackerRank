import math


def count_triplets(factor, data):
    triplets = 0
    if factor == 1:
        for num in data:
            triplets += nCr(data.get(num), 3)
        return triplets
    for num in data:
        if data.get(num * factor) and data.get(num * factor * factor):
            triplets += (data.get(num) * data.get(num * factor) *
                         data.get(num * factor * factor))
            data[num] = 0
    return triplets


def nCr(n, r):
    f = math.factorial
    return f(n) // f(r) // f(n - r)


prob_details = list(map(int, input().rstrip().split()))
array = list(map(int, input().rstrip().split()))

data = {}
for element in array:
    if data.get(element):
        data[element] += 1
    else:
        data[element] = 1

print(count_triplets(factor=prob_details[1], data=data))
