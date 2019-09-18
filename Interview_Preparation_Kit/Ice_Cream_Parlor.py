

def find_ice_cream_ids(array, money):
    cost_dict = {}
    for index, data in enumerate(array):
        if data in cost_dict:
            cost_dict[data].append(index + 1)
        else:
            cost_dict[data] = [index + 1]

    unique_numbers = list(cost_dict.keys())
    result = []
    for element in unique_numbers:
        temp_diff = money - element
        if temp_diff == element and len(cost_dict[element]) < 2:
            continue
        elif temp_diff in cost_dict:
            result.append(str(cost_dict[element][0]))
            if element == temp_diff:
                result.append(str(cost_dict[element][1]))
            else:
                result.append(str(cost_dict[temp_diff][0]))
            break
    # Sort the result
    result.sort()
    return ' '.join(result)


#############
trips = int(input())
for _ in range(trips):
    money = int(input())
    array_size = int(input())
    array = list(map(int, input().split(' ')))
    print(find_ice_cream_ids(array=array, money=money))
#############
