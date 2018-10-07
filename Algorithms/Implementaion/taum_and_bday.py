
def calc_minimum_cost(black_white_count, black_white_cost, test_cases):
    """
    Method to calculate minimum cost required to buy
    gifts

    Args:
            black_white_count: Array[0] block count, Array[0] white count
            black_white_cost: Array[0] block cost, Array[0] white cost,
                                              conversion cost
            test_cases: Number of testcases
    Rrturn:
            None
    """
    for index in xrange(0, test_cases):
        if black_white_cost[index][0] > (black_white_cost[index][1] +
                                         black_white_cost[index][2]):
            cost = (black_white_count[index][0] * (
                black_white_cost[index][1] + black_white_cost[index][2]
            )) + (black_white_count[index][1] * black_white_cost[index][1])
        elif black_white_cost[index][1] > (black_white_cost[index][0] +
                                           black_white_cost[index][2]):
            cost = (black_white_count[index][1] * (
                black_white_cost[index][0] + black_white_cost[index][2]
            )) + (black_white_count[index][0] * black_white_cost[index][0])
        else:
            cost = (
                black_white_count[index][0] * black_white_cost[index][0]
            ) + (
                black_white_count[index][1] * black_white_cost[index][1]
            )
        print cost
    return 1


############
test_cases = int(raw_input())
black_white_count = []
black_white_cost = []
for _ in xrange(0, test_cases):
    black_white_count.append(map(int, raw_input().rstrip().split()))
    black_white_cost.append(map(int, raw_input().rstrip().split()))

calc_minimum_cost(black_white_count, black_white_cost, test_cases)
############
