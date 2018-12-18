

def calc_max_distance(array, no_of_cities):
    distance_array = []
    for city in xrange(0, no_of_cities):
        if city in array:
            pass
        else:
            distance_array.append(
                calc_nearby_station(
                    array=array, city=city
                )
            )

    return 0 if not distance_array else max(distance_array)


def calc_nearby_station(array, city):
    low = city - 1
    high = city + 1
    while True:
        if low in array:
            return city - low
        elif high in array:
            return high - city
        else:
            low -= 1
            high += 1


my_input = map(int, raw_input().rstrip().split(' '))
array = map(int, raw_input().split(' '))


print calc_max_distance(
    array=array, no_of_cities=my_input[0]
)
