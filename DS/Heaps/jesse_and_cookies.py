Heap = list()


def add_element(element):
    Heap.append(element)
    size = len(Heap)
    _swim_up(element=size)


def heapify():
    size = len(Heap)
    for index in reversed(range((size // 2) - 1)):
        _swim_down(parent=index, size=size - 1)


def _swim_down(parent, size):
    lchild_index = (2 * parent) + 1
    rchild_index = (2 * parent) + 2
    l_index = parent
    if lchild_index <= size and Heap[lchild_index] < Heap[parent]:
        l_index = lchild_index
    if rchild_index <= size and Heap[rchild_index] < Heap[l_index]:
        l_index = rchild_index
    if l_index != parent:
        swap_element(index1=l_index, index2=parent)
        _swim_down(parent=l_index, size=size)


def _swim_up(element):
    if element == 1:
        return
    parent = (element // 2)
    if Heap[element - 1] < Heap[parent - 1]:
        swap_element(index1=element - 1, index2=parent - 1)
        _swim_up(element=parent - 1)


def extract_root():
    size = len(Heap)
    swap_element(index1=0, index2=size - 1)
    result = Heap.pop()
    _swim_down(parent=0, size=size - 2)
    return result


def swap_element(index1, index2):
    temp = Heap[index1]
    Heap[index1] = Heap[index2]
    Heap[index2] = temp


def find_cookie_sweetness(K):
    result = 0
    while Heap[0] < K and len(Heap) > 1:
        root1 = extract_root()
        root2 = extract_root()
        add_element(element=((1 * root1) + (2 * root2)))
        result += 1

    if len(Heap) == 1 and Heap[0] < K:
        return -1
    return result


if __name__ == "__main__":
    temp = list(map(int, input().split()))
    N, K = temp[0], temp[1]
    Heap = list(map(int, input().split()))
    heapify()
    print(find_cookie_sweetness(K))
