

def find_minimum_cost_to_convert(magic_square):
    positions = [
        [0, 0], [0, 1], [0, 2], [1, 2]
    ]
    opp_positions = [
        [2, 2], [2, 1], [2, 0], [1, 0]
    ]
    minimum_cost = 0
    if magic_square[1][1] != 5:
        minimum_cost += abs(magic_square[1][1] - 5)
    for index in range(4):
        start = positions[index]
        end = opp_positions[index]
        start_num = magic_square[start[0]][start[1]]
        end_num = magic_square[end[0]][end[1]]
        pending_diff = abs(10 - (start_num + end_num))
        if pending_diff > 0:
            minimum_cost += pending_diff
    return minimum_cost


MAGIC_SQUARE = []
for _ in range(3):
    MAGIC_SQUARE.append(list(map(int, input().split())))

print(find_minimum_cost_to_convert(magic_square=MAGIC_SQUARE))
