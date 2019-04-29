

def starnge_counter(time):
    start = 1
    counter = 3
    if time == 1:
        return 3
    while start < time:
        start += counter
        counter = counter * 2
        if start == time:
            return counter
    counter = counter // 2
    start = start - counter
    return counter - (time - start)


time = int(input())
print(starnge_counter(time))
