

def calc_queens_attack_count(n, queen_position, obstacles, obstacles_count):
    """
    Method to calculate queens attack possiblites in
    an given n * n square
    """
    """ calc all possible moves of queen """
    possible_up = n - queen_position[0]
    possible_down = queen_position[0] - 1
    possible_right = n - queen_position[1]
    possible_left = queen_position[1] - 1
    possible_right_up = min(n - queen_position[0], n - queen_position[1])
    possible_left_up = min(n - queen_position[0], queen_position[1] - 1)
    possible_right_down = min(queen_position[0] - 1, n - queen_position[1])
    possible_left_down = min(queen_position[0] - 1, queen_position[1] - 1)
    ########################################
    for obs in obstacles:
        if obs[0] == queen_position[0] and obs[1] > queen_position[1]:
            right_temp = (obs[1] - queen_position[1]) - 1
            if right_temp < possible_right:
                possible_right = right_temp
        elif obs[0] == queen_position[0] and obs[1] < queen_position[1]:
            left_temp = (queen_position[1] - obs[1]) - 1
            if left_temp < possible_left:
                possible_left = left_temp
        elif obs[1] == queen_position[1] and obs[0] > queen_position[0]:
            up_temp = (obs[0] - queen_position[0]) - 1
            if up_temp < possible_up:
                possible_up = up_temp
        elif obs[1] == queen_position[1] and obs[0] < queen_position[0]:
            down_temp = (queen_position[0] - obs[0]) - 1
            if down_temp < possible_down:
                possible_down = down_temp
        elif check_diagonal(queen_position, obs):
            if obs[0] > queen_position[0] and obs[1] > queen_position[1]:
                right_up_temp = (obs[0] - queen_position[0]) - 1
                if right_up_temp < possible_right_up:
                    possible_right_up = right_up_temp
            elif obs[0] < queen_position[0] and obs[1] < queen_position[1]:
                left_down_temp = (queen_position[0] - obs[0]) - 1
                if left_down_temp < possible_left_down:
                    possible_left_down = left_down_temp
            elif obs[0] > queen_position[0] and obs[1] < queen_position[1]:
                left_up_temp = (obs[0] - queen_position[0]) - 1
                if left_up_temp < possible_left_up:
                    possible_left_up = left_up_temp
            else:
                right_down_temp = (queen_position[0] - obs[0]) - 1
                if right_down_temp < possible_right_down:
                    possible_right_down = right_down_temp

    # Calculate possible moves of the queen
    possible_moves = possible_up + possible_down + possible_right \
        + possible_left + possible_right_up + possible_left_up \
        + possible_right_down + possible_left_down
    return possible_moves


def check_diagonal(coord1, coord2):
    if abs(coord1[0] - coord2[0]) == abs(coord1[1] - coord2[1]):
        return True
    else:
        return False


##############
temp = raw_input().split()
n = int(temp[0])
obstacles_count = int(temp[1])
obstacles = []
queen_position = map(int, raw_input().rstrip().split())
for _ in xrange(0, obstacles_count):
    obstacles.append(map(int, raw_input().rstrip().split()))

print calc_queens_attack_count(n, queen_position, obstacles, obstacles_count)
##############
