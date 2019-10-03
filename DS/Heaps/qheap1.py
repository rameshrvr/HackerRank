

Heap = list()


def add_element(element):
    size = len(Heap)
    Heap.append(element)
    _swim_up(element=size)


def delete_element(element):
    elem_index = find_element_index(element=element)
    Heap[elem_index] = float("-inf")
    _swim_up(element=elem_index)
    extract_root()


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
    if element == 0:
        return
    parent = (element // 2)
    if Heap[element] < Heap[parent]:
        swap_element(index1=element, index2=parent)
        _swim_up(element=parent)


def extract_root():
    size = len(Heap)
    swap_element(index1=0, index2=size - 1)
    result = Heap.pop()
    _swim_down(parent=0, size=size - 2)
    return result


def find_element_index(element):
    size = len(Heap)
    for index in range(size):
        if Heap[index] == element:
            return index
    return False


def swap_element(index1, index2):
    temp = Heap[index1]
    Heap[index1] = Heap[index2]
    Heap[index2] = temp


if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        data = list(map(int, input().split()))
        if data[0] == 1:
            add_element(element=data[1])
        elif data[0] == 2:
            delete_element(element=data[1])
        else:
            print(Heap[0])
