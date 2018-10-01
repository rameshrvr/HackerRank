

def calc_alice_rank(
        score_board, alice_score
):
    """
    Method to calculate alice rank after every game
    """
    sorted_score_board = list(reversed(list(sorted(set(score_board)))))
    score_board_size = len(sorted_score_board)
    for score in alice_score:
        if score >= sorted_score_board[0]:
            print '{}'.format(1)
        else:
            for index in xrange(0, score_board_size - 1):
                if index == score_board_size - 1:
                    print '{}'.format(index + 2)
                    break
                elif sorted_score_board[index] > score >= sorted_score_board[index + 1]:
                    print '{}'.format(index + 2)
                    break
                elif sorted_score_board[index] >= score >= sorted_score_board[index + 1]:
                    print '{}'.format(index + 1)
                    break
                elif sorted_score_board[score_board_size - 1] > score:
                    print '{}'.format(score_board_size + 1)
                    break


############
score_board_size = int(raw_input())
score_board = map(int, raw_input().rstrip().split(' '))
alice_games = int(raw_input())
alice_score = map(int, raw_input().rstrip().split(' '))

calc_alice_rank(score_board, alice_score)
############
