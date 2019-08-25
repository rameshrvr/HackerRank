from collections import deque


def max_possible_score(stack1, stack2, X):
    queue1 = deque(stack1)
    queue2 = deque(stack2)
    possible_score = 0
    overall_sum = 0
    while True:
        if (not queue1) or (not queue2):
            break
        if queue1[0] > queue2[0]:
            score = queue2.popleft()
            if (overall_sum + score) <= X:
                overall_sum += score
                possible_score += 1
            else:
                break
        else:
            score = queue1.popleft()
            if (overall_sum + score) <= X:
                overall_sum += score
                possible_score += 1
            else:
                break
    return possible_score


#####################
no_of_games = int(input())

for _ in range(no_of_games):
    details = list(map(int, input().split()))
    N, M, X = details[0], details[1], details[2]

    stack1 = list(map(int, input().split()))
    stack2 = list(map(int, input().split()))
    print(max_possible_score(stack1, stack2, X))
#####################
