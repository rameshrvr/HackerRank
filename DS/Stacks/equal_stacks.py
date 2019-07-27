from collections import deque


def get_equal_stacks_heights(
        stack1_data, stack2_data, stack3_data
):
    """
    stack_sizes: Array of stack1, stack2, stack3 sizes
    """
    stack_heights = []
    stack_heights.append(calc_stack_height(stack1_data))
    stack_heights.append(calc_stack_height(stack2_data))
    stack_heights.append(calc_stack_height(stack3_data))
    if stack_heights[0] == stack_heights[1] == stack_heights[2]:
        return stack_heights[0]
    queue1 = deque(stack1_data)
    queue2 = deque(stack2_data)
    queue3 = deque(stack3_data)
    max_height = get_smallest(
        stack_heights[0], stack_heights[1], stack_heights[2]
    )
    while (queue1 != [] and queue2 != [] and queue3 != []):
        if stack_heights[0] > max_height:
            stack1_elem = queue1.popleft()
            stack_heights[0] -= stack1_elem
        if stack_heights[1] > max_height:
            stack2_elem = queue2.popleft()
            stack_heights[1] -= stack2_elem
        if stack_heights[2] > max_height:
            stack3_elem = queue3.popleft()
            stack_heights[2] -= stack3_elem
        max_height = get_smallest(
            stack_heights[0], stack_heights[1], stack_heights[2]
        )
        if stack_heights[0] == stack_heights[1] == stack_heights[2]:
            break
    return stack_heights[0]


def calc_stack_height(stack):
    height = 0
    for data in stack:
        height += data
    return height


def get_smallest(data1, data2, data3):
    if data1 < data2:
        if data1 < data3:
            return data1
        else:
            return data3
    else:
        if data2 < data3:
            return data2
        else:
            return data3


#####################
stacks = list(map(int, input().split()))
stack1_size, stack2_size, stack3_size = stacks[0], stacks[1], stacks[2]

stack1_data = list(map(int, input().split()))
stack2_data = list(map(int, input().split()))
stack3_data = list(map(int, input().split()))

print(get_equal_stacks_heights(
    stack1_data=stack1_data, stack2_data=stack2_data,
    stack3_data=stack3_data))
#####################
