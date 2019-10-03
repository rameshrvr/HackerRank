

def counting_numbers(array, N):
    num_dict = {}
    for number in array:
        if number in num_dict:
            num_dict[number] += 1
        else:
            num_dict[number] = 1

    resut_list = []
    for index in range(N):
        if index in num_dict:
            resut_list.append(str(num_dict[index]))
        else:
            resut_list.append(str(0))

    return ' '.join(resut_list)


###
N = int(input())
array = list(map(int, input().split()))
print(counting_numbers(array, N))
###
