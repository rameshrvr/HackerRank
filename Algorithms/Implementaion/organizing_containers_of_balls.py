

def is_organizing_possible(data_container, size):
    row_sum = []
    column_sum = []
    for row_index in range(size):
        temp_row_sum = 0
        temp_colum_sum = 0
        for column_index in range(size):
            temp_row_sum += data_container[row_index][column_index]
            temp_colum_sum += data_container[column_index][row_index]
        row_sum.append(temp_row_sum)
        column_sum.append(temp_colum_sum)

    check_index_list = list(range(size))
    result = 'Possible'
    for index in range(size):
        for data in check_index_list:
            if check_empty(
                row_sum=row_sum[index], column_sum=column_sum[data],
                data_position=data_container[index][data]
            ):
                check_index_list.remove(data)
                break
        else:
            result = 'Impossible'
            break

    return result


def check_empty(row_sum, column_sum, data_position):
    if abs(data_position - row_sum) == abs(data_position - column_sum):
        return True
    else:
        return False


queries = int(input())

for _ in range(queries):
    data_container = []
    no_of_container = int(input())
    for _ in range(no_of_container):
        data_container.append(
            list(map(int, input().split()))
        )
    print(is_organizing_possible(
        data_container=data_container, size=no_of_container
    ))
