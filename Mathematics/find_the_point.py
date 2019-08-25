

def find_reflection_point(x, r):
    # Formula for finding mid-point
    # points (x1, x2) (y1, y2)
    # Midpoint r1 = (x1 + y1) / 2, r2 = (x2 + y2) / 2
    # So for the given midpoint the end point formula is
    # y1 = (2 * r1) - x1 and y2 = (2 * r2) - x2

    y1 = (2 * r[0]) - x[0]
    y2 = (2 * r[1]) - x[1]
    return '{} {}'.format(y1, y2)


#################
testcases = int(input())
for _ in range(testcases):
    data = list(map(int, input().split()))
    print(find_reflection_point(
        x=[data[0], data[1]],
        r=[data[2], data[3]]
    ))
#################
