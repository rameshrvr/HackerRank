

def find_cavity_map(grid, grid_size):
    for row in range(1, grid_size - 1):
        for column in range(1, grid_size - 1):
            temp = int(grid[row][column])
            if (
                grid[row - 1][column] != 'X'
            ) and (
                grid[row][column - 1] != 'X'
            ) and (
                grid[row][column + 1] != 'X'
            ) and (
                grid[row + 1][column] != 'X'
            ) and (
                int(grid[row - 1][column]) < temp
            ) and (
                int(grid[row][column - 1]) < temp
            ) and (
                int(grid[row][column + 1]) < temp
            ) and (
                int(grid[row + 1][column]) < temp
            ):
                grid[row][column] = 'X'
    return grid


my_input = int(raw_input())
grid = []
for _ in range(my_input):
    grid.append(list(raw_input().rstrip()))


output = find_cavity_map(grid=grid, grid_size=my_input)
for row in range(0, my_input):
    print ''.join(output[row])
