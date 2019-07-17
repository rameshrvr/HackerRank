

def calc_price_of_the_toy(rows, columns, data):
    matrix_row = rows - 1
    matrix_column = columns - 1
    price_of_toy = 0
    for row_index in range(rows):
        for column_index in range(columns):
            price_of_toy += 2

            if (row_index == 0 or row_index == matrix_row) and\
                    (column_index == 0 or column_index == matrix_column):
                if rows == 1 and columns == 1:
                    price_of_toy += 4 * data[row_index][column_index]
                elif rows == 1 or columns == 1:
                    price_of_toy += 3 * data[row_index][column_index]
                else:
                    price_of_toy += 2 * data[row_index][column_index]

            if row_index == 0 or row_index == matrix_row:
                if column_index != 0 and column_index != matrix_column:
                    if rows == 1:
                        price_of_toy += 2 * data[row_index][column_index]
                    else:
                        price_of_toy += data[row_index][column_index]

            if column_index == 0 or column_index == matrix_column:
                if row_index != 0 and row_index != matrix_row:
                    if columns == 1:
                        price_of_toy += 2 * data[row_index][column_index]
                    else:
                        price_of_toy += data[row_index][column_index]

            if column_index != matrix_column:
                price_of_toy += abs(data[row_index][column_index] -
                                    data[row_index][column_index + 1])

            if row_index != matrix_row:
                price_of_toy += abs(data[row_index][column_index] -
                                    data[row_index + 1][column_index])

    return price_of_toy


##################
prob_details = list(map(int, input().split()))
rows = prob_details[0]
columns = prob_details[1]
prob_data = []
for _ in range(rows):
    prob_data.append(list(map(int, input().split())))
print(calc_price_of_the_toy(rows=rows, columns=columns, data=prob_data))
##################
