

def jumping_on_cloud(data, data_size, k):
    energy = 100
    start = 0
    reached = 0
    while reached == 0:
        position = start + k
        if position >= data_size:
            start = position - data_size
            position = 0
        if data[position] == 1:
            energy -= 2
        energy -= 1
        start = position
        if position == 0:
            break
    return energy


details = list(map(int, input().split()))
data = list(map(int, input().split()))

print(jumping_on_cloud(data=data, data_size=details[0], k=details[1]))
