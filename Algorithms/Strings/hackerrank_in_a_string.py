

def hackerrankInString(char_list):
    hackerrank = list('hackerrank')
    for char in hackerrank:
        for index in range(len(char_list)):
            if char == char_list[index]:
                char_list = char_list[index + 1:]
                break
        else:
            return 'NO'
    return 'YES'


test_cases = int(input())
str_array = []
for _ in range(test_cases):
    string = input()
    print(hackerrankInString(char_list=list(string)))
