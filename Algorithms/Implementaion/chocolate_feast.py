

def ChocolateFeast(amout, cost, trade):
    """
            Method to calculate the number of choco Little
            bobby ate

            @param amout: total amout he got in his hand
            @param cost: cost of a single choco
            @param trade: No of wrappers needed to get one choco
    """
    total_choco = amount / cost
    wrappers = total_choco
    while wrappers >= trade:
        new_wrapper = wrappers / trade
        total_choco += new_wrapper
        wrappers = (wrappers - (trade * new_wrapper)) + new_wrapper

    return total_choco


test_cases = int(raw_input())
for _ in range(test_cases):
    amount, cost, trade = map((lambda x: int(x)), (raw_input().split()))
    print ChocolateFeast(amount, cost, trade)
