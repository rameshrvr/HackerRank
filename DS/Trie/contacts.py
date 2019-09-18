

class Trie():
    def __init__(self, char=None):
        self.char = char
        self.children = {}
        self.count = 1
        self.children['end'] = False


def add_string(root, string):
    current_node = root
    for char in list(string):
        if char in current_node.children:
            current_node.children[char].count += 1
        else:
            current_node.children[char] = Trie(char)
        current_node = current_node.children[char]
    current_node.children['end'] = True


def search_string(root, string):
    current_node = root
    for char in list(string):
        if char in current_node.children:
            current_node = current_node.children[char]
        else:
            return False
    return True if current_node.children['end'] is True else False


def search_prefix(root, string):
    current_node = root
    for char in list(string):
        if char in current_node.children:
            current_node = current_node.children[char]
        else:
            return 0
    return current_node.count


if __name__ == "__main__":
    size = int(input())
    trie = Trie()
    for _ in range(size):
        strings = list(input().split())
        if strings[0] == 'add':
            add_string(root=trie, string=strings[1])
        else:
            print(search_prefix(root=trie, string=strings[1]))
