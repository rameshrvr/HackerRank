

def find_pairs(K, data):
    data_dict = {}
    result = 0
    for element in data:
        if element in data_dict:
            data_dict[element] += 1
        else:
            data_dict[element] = 1

    for ind_data in list(data_dict.keys()):
        pair = K + ind_data
        if pair in data_dict:
            result += (data_dict[ind_data] * data_dict[pair])
    return result


#########
temp = list(map(int, input().split()))
data = list(map(int, input().split()))
size, K = temp[0], temp[1]
print(find_pairs(K, data))
#########
