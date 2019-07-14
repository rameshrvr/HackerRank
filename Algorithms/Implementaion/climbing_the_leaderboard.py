

def calc_alice_rank(
    score_board, alice_score, alice_games
):
    score_board_hash = {}
    for score in score_board:
        if score in score_board_hash:
            continue
        else:
            score_board_hash[score] = 1
    score_board = list(score_board_hash.keys())

    alice_score_hash = {}
    for score in alice_score:
        if score in alice_score_hash:
            alice_score_hash[score] += 1
        else:
            alice_score_hash[score] = 1

    alice_rank_counter = 0
    for index in reversed(range(len(score_board))):
        if alice_rank_counter >= alice_games:
            break
        while alice_score[alice_rank_counter] <= score_board[index]:
            current_score = alice_score[alice_rank_counter]
            if score_board[index] == current_score:
                for _ in range(alice_score_hash[current_score]):
                    print(index + 1)
                alice_rank_counter += alice_score_hash[current_score]
            elif score_board[index] > current_score:
                for _ in range(alice_score_hash[current_score]):
                    print(index + 2)
                alice_rank_counter += alice_score_hash[current_score]
            elif index == 0 and current_score > score_board[index]:
                print(1)
                alice_rank_counter += 1
            if alice_rank_counter >= alice_games:
                break

        if index == 0:
            for _ in range(alice_games - alice_rank_counter):
                print(1)


############
score_board_size = int(input())
score_board = list(map(int, input().split()))
alice_games = int(input())
alice_score = list(map(int, input().split()))

calc_alice_rank(score_board, alice_score, alice_games)
############
