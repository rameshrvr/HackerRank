

class Trie():
    """
    """

    def __init__(self, char=None):
        self.char = char
        self.children = {}
        self.count = 1
        self.children['end'] = False


def add_string(root, string):
    """
    Brief:
        Method to Add a string to Trie.
    Args:
        root: object that represends root Trie node
        string: String to add
    Return: None
    Example:
        trie = Trie()
        add_string(root=trie, string='abc')
        # The trie will look somethink like this
        ipdb> trie.children
            {'end': False, 'a': <__main__.Trie object at 0x1075b0a20>}
        ipdb> trie.children['a'].children
            {'end': False, 'b': <__main__.Trie object at 0x1075b0a58>}
        ipdb> trie.children['a'].count
            1
        ipdb> trie.children['a'].children['b'].children
            {'end': False, 'c': <__main__.Trie object at 0x1075b0a90>}
        ipdb> trie.children['a'].children['b'].count
            1
        ipdb> trie.children['a'].children['b'].children['c'].children
            {'end': True}
        ipdb> trie.children['a'].children['b'].children['c'].count
            1
    """
    current_node = root
    for char in list(string):
        if char in current_node.children:
            current_node.children[char].count += 1
        else:
            current_node.children[char] = Trie(char)
        current_node = current_node.children[char]
    current_node.children['end'] = True


def search_string(root, string):
    """
    Brief:
        Search weather the given is present in the Trie
    Args:
        root: object that represends root Trie node
        string: String to search
    Returns:
        'True' if the string is found 'False' otherwise
    """
    current_node = root
    for char in list(string):
        if char in current_node.children:
            current_node = current_node.children[char]
        else:
            return False
    return True if current_node.children['end'] is True else False


def search_prefix(root, string):
    """
    Brief:
        Search the prefix in Trie and return count. Here the count is
        for how many strings the given is a prefix
    Args:
        root: object that represends root Trie node
        string: Prefix to search
    Returns:
        Count of the prefix. 0 if the prefix not found
    """
    current_node = root
    for char in list(string):
        if char in current_node.children:
            current_node = current_node.children[char]
        else:
            return 0
    return current_node.count


def delete_string(root, string):
    """
    Brief:
        Delete the given string from Trie
    Args:
        root: object that represends root Trie node
        string: String to delete
    Returns:
        True if the string is deleted. False if the string
        not present in the Trie.
    """
    current_node = root
    if search_string(root=root, string=string):
        for char in list(string):
            if current_node.children[char].count == 1:
                current_node.children.pop(char, None)
                break
            current_node.children[char].count -= 1
            current_node = current_node.children[char]
        else:
            current_node.children['end'] = False
    else:
        return False
    return True


if __name__ == "__main__":
    trie = Trie()
    add_string(root=trie, string='abc')
    add_string(root=trie, string='fgh')
    add_string(root=trie, string='apple')
    add_string(root=trie, string='abco')
    search_string(root=trie, string='apple')  # => True
    search_string(root=trie, string='appl')  # => False
    search_prefix(root=trie, string='app')  # => 1
    search_prefix(root=trie, string='ab')  # => 2
    delete_string(root=trie, string='abco')  # => True
    delete_string(root=trie, string='app')  # => False
    delete_string(root=trie, string='orange')   # => False
