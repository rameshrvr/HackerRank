
CHAR_ARRAY = list(map(chr, range(97, 123)))
STR_WEIGHT = {value: key + 1 for key, value in enumerate(CHAR_ARRAY)}
SUB_STR_WEIGHT = {}


def get_sub_str_weight(data_str):
    data_str = list(data_str)
    counter_weight = 0
    for index in range(len(data_str)):
        weight = 0
        char_weight = 0
        if index == 0:
            weight = STR_WEIGHT[data_str[index]]
        else:
            if data_str[index] == data_str[index - 1]:
                counter_weight += STR_WEIGHT[data_str[index]]
                char_weight = STR_WEIGHT[data_str[index]]
            else:
                counter_weight = 0
                char_weight = STR_WEIGHT[data_str[index]]
            weight = counter_weight + char_weight

        SUB_STR_WEIGHT[weight] = 1
    return SUB_STR_WEIGHT


def process_query(weight):
    if weight in SUB_STR_WEIGHT:
        return 'Yes'
    else:
        return 'No'


string = input()
queries = int(input())
get_sub_str_weight(data_str=string)

for _ in range(queries):
    data = int(input())
    print(process_query(weight=data))
