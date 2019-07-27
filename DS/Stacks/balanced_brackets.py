
def is_balanced(string):
    stack = []
    str_list = list(string)
    bracket_dict = {
        '{': '}', '[': ']', '(': ')'
    }
    for bracket in str_list:
        if bracket == '{' or bracket == '[' or bracket == '(':
            stack.append(bracket)
        else:
            if not stack:
                return 'NO'
            open_bracket = stack.pop()
            if bracket != bracket_dict[open_bracket]:
                return 'NO'
    return 'YES' if not stack else 'NO'


#################
no_of_strings = int(input())

for _ in range(no_of_strings):
    string = input()
    print(is_balanced(string))

#################
