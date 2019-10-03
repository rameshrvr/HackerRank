

def design_door_mat(N, M):
    middle = (N // 2)
    designer_mat = []
    for number in range(middle):
        _design = ((2 * number) + 1)
        _size = (M - (_design * 3)) // 2
        designer_mat.append(
            '{0}{1}{0}'.format('-' * _size, _design * '.|.')
        )
    designer_mat.append('{0}{1}{0}'.format('-' * ((M - 7) // 2), 'WELCOME'))
    for number in reversed(range(middle)):
        designer_mat.append(designer_mat[number])
    return designer_mat


######
temp = list(map(int, input().split()))
N, M = temp[0], temp[1]
designer_mat = design_door_mat(N, M)
for row in designer_mat:
    print(row)
######
