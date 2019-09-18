

class Trie():
    def __init__(self, char=None):
        self.char = char
        self.children = {}
        self.count = 1
        self.children['end'] = False


def add_string(root, string):
    if_prefix = False
    current_node = root
    for char in list(string):
        if char in current_node.children:
            current_node.children[char].count += 1
            if current_node.children[
                char
            ].count > 1 and current_node.children[
                char
            ].children['end'] is True:
                if_prefix = True
        else:
            current_node.children[char] = Trie(char)
        current_node = current_node.children[char]
    current_node.children['end'] = True
    if current_node.count > 1:
        return True
    return if_prefix


#########
N = int(input())
trie = Trie()
is_good_set = True
bad_set_value = ''
for _ in range(N):
    string = input()
    if is_good_set:
        data = add_string(root=trie, string=string)
        if data:
            is_good_set = False
            bad_set_value = string


if is_good_set:
    print('GOOD SET')
else:
    print('BAD SET')
    print(bad_set_value)
#########
