

def calc_max_distance(
    space_station_details, total_space_station, total_cities
):
    max_distance = 0
    space_station_details.sort()
    for index in range(total_space_station - 1):
        distance = int(
            (space_station_details[index + 1] -
             space_station_details[index]) / 2
        )
        if distance > max_distance:
            max_distance = distance
    # Distance of last city from space station
    distance = int(
        ((total_cities - 1) -
         space_station_details[total_space_station - 1])
    )
    if distance > max_distance:
        max_distance = distance
    # Distance of first city from space station
    distance = int((space_station_details[0] - 0))
    if distance > max_distance:
        max_distance = distance
    return max_distance


details = list(map(int, input().split()))
total_cities, total_space_station = details[0], details[1]

space_station_details = list(map(int, input().split()))


print(
    calc_max_distance(
        space_station_details=space_station_details,
        total_space_station=total_space_station,
        total_cities=total_cities
    )
)
