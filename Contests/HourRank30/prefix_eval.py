def prefix_evaluate(array):
    stack = []
    for t in reversed(array):
        if t == '+':
            stack[-2:] = [int(stack[-1]) + int(stack[-2])]
        elif t == '-':
            stack[-2:] = [int(stack[-1]) - int(stack[-2])]
        elif t == '*':
            stack[-2:] = [int(stack[-1]) * int(stack[-2])]
        elif t == '/':
            stack[-2:] = [int(stack[-1]) / int(stack[-2])]
        else:
            stack.append(t)
    return stack[0]


########
string = list(raw_input())
print prefix_evaluate(string)
########
