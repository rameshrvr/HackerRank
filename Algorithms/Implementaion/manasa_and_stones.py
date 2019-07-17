

def get_possible_values_of_last_stone(
    no_of_stones, first_difference, second_difference
):
    if first_difference > second_difference:
        first_difference, second_difference = second_difference, first_difference
    first_possible_stone_value = first_difference * (no_of_stones - 1)
    last_possible_stone_value = second_difference * (no_of_stones - 1)
    if first_difference == second_difference:
        return first_possible_stone_value
    possible_stone_values = []
    possible_stone_values.append(str(first_possible_stone_value))
    stone_cache = first_possible_stone_value
    # Find middle values of possible stone value
    for _ in range(no_of_stones - 2):
        possible_stone = stone_cache - first_difference + second_difference
        possible_stone_values.append(str(possible_stone))
        stone_cache = possible_stone
    possible_stone_values.append(str(last_possible_stone_value))
    return ' '.join(possible_stone_values)


test_cases = int(input())

for _ in range(test_cases):
    no_of_stones = int(input())
    first_difference = int(input())
    second_difference = int(input())
    print(
        get_possible_values_of_last_stone(
            no_of_stones=no_of_stones,
            first_difference=first_difference,
            second_difference=second_difference
        )
    )
