

def happy_lady_bugs(board_game, board_size):
    board_game_list = list(board_game)
    board_game_hash = {}
    for data in board_game_list:
        if data in board_game_hash:
            board_game_hash[data] += 1
        else:
            board_game_hash[data] = 1
    # Check for singe bug
    for data in board_game_hash.keys():
        if data != '_' and board_game_hash[data] == 1:
            return 'NO'

    # Check for un-happy lady bugs
    if '_' not in board_game_hash:
        for index in range(1, board_size - 1):
            if board_game_list[index - 1] != board_game_list[index] and\
                    board_game_list[index] != board_game_list[index + 1]:
                return 'NO'
    return 'YES'


no_of_games = int(input())

for _ in range(no_of_games):
    str_size = int(input())
    board_game = input()
    print(happy_lady_bugs(board_game=board_game, board_size=str_size))
