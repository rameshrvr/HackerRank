
prob_data = list(map(int, input().split()))
row, column, k = prob_data[0], prob_data[1], prob_data[2]

CITY_NETWORK = {}
TOTAL_POSTS = [column * row]


def update_city_network(row, column1, column2):
    if row in CITY_NETWORK:
        pass
    else:
        CITY_NETWORK[row] = [column, 0]
    if CITY_NETWORK[row][0] > column1:
        CITY_NETWORK[row][0] = column1
    if CITY_NETWORK[row][1] < column2:
        CITY_NETWORK[row][1] = column2


def calc_lampposts_count():
    for key, value in CITY_NETWORK.items():
        track_count = (value[1] - value[0]) + 1
        TOTAL_POSTS[0] -= track_count


for _ in range(k):
    prob_data = list(map(int, input().split()))
    update_city_network(
        row=prob_data[0], column1=prob_data[1], column2=prob_data[2]
    )

calc_lampposts_count()

print(TOTAL_POSTS[0])
