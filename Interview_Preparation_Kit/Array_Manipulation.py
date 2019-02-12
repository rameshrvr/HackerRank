

def array_manipulation(start, end, add):
    array[start - 1] += add
    array[end] -= add


details = list(map(int, input().split(' ')))
array = [0] * (details[0] + 1)
data = []
for _ in range(details[1]):
    _data = list(map(int, input().split(' ')))
    array_manipulation(
        start=_data[0], end=_data[1], add=_data[2]
    )

max_sum = 0
maximum = 0

for i in array:
    max_sum += i
    if (max_sum > maximum):
        maximum = max_sum

print(maximum)
