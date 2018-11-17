

def get_maximum_games_you_can_buy(
        starting_prize, diff, minimum_amount, amount_in_hand
):
    result = 0
    amount_spend = starting_prize
    while amount_spend <= amount_in_hand:
        if (starting_prize - diff) > minimum_amount:
            starting_prize -= diff
        else:
            starting_prize = minimum_amount
        amount_spend += starting_prize
        result += 1
    return result


##############
temp = map(int, raw_input().strip().split())
starting_prize = temp[0]
diff = temp[1]
minimum_amount = temp[2]
amount_in_hand = temp[3]

print get_maximum_games_you_can_buy(
    starting_prize, diff, minimum_amount, amount_in_hand
)
##############
