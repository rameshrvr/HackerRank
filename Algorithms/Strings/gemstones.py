

def get_gemstone_count(data):
    hash_array = []
    for data_string in data:
        temp_hash = {}
        data_string_list = list(data_string)
        for char in data_string_list:
            if char not in temp_hash:
                temp_hash[char] = 1
        hash_array.append(temp_hash)

    first_hash = hash_array.pop(0)
    gemstones = 0
    for key in first_hash.keys():
        temp_counter = 1
        for item in hash_array:
            if key in item:
                continue
            else:
                temp_counter = 0
                break
        if temp_counter == 1:
            gemstones += 1
    return gemstones


####################
arr_size = int(input())
string_array = []
for _ in range(arr_size):
    string_array.append(input())
print(get_gemstone_count(data=string_array))
####################
