
def calc_number_of_supplies(n, m):
    return int(((n + (n % 2)) * (m + (m % 2))) / 4)


#################
temp = list(map(int, input().split()))
n, m = temp[0], temp[1]
print(calc_number_of_supplies(n, m))
#################
