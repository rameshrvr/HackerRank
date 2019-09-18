from collections import deque

dqueue = deque()


def perform_operations(op_data):
    if op_data[0] == 1:
        dqueue.append(op_data[1])
    elif op_data[0] == 2:
        dqueue.popleft()
    else:
        print(dqueue[0])


####
queries = int(input())
for _ in range(queries):
    in_data = list(map(int, input().split(' ')))
    perform_operations(op_data=in_data)
####
