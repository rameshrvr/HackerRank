
def print_number_square_wall(n, starting_number):
    """
    """
    array = [[0 for x in range(n)] for y in range(n)]
    array[0][0] = starting_number
    starting_number += 1
    for index in xrange(1, n):
        column = index
        row = 0
        while column > 0:
            if row < column:
                array[row][column] = starting_number
                starting_number += 1
                row += 1
            elif row == column:
                array[row][column] = starting_number
                starting_number += 1
                column -= 1
            else:
                array[row][column] = starting_number
                starting_number += 1
                column -= 1
        array[row][column] = starting_number
        starting_number += 1

    # Print the array
    for index in xrange(0, n):
        print ' '.join(map(str, array[index]))
    return


############
temp = map(int, raw_input().rstrip().split())
n = temp[0]
starting_number = temp[1]

print_number_square_wall(n, starting_number)
############
