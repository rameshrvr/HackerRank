
class SortTheArray(object):
    def __init__(self, array):
        self.array = array
        self.array.sort(key=lambda x: x[1], reverse=True)

    def sort_by_name(self):
        index = 0
        while index < (len(self.array) - 1):
            temp_index = index
            if self.array[index][1] == self.array[index + 1][1]:
                temp_index += 1
                while self.array[index][1] == self.array[temp_index][1]:
                    temp_index += 1
                self.array[index:temp_index] = sorted(
                    self.array[index:temp_index], key=lambda x: x[0]
                )
                index += temp_index
            else:
                index += 1
        return self.array


size = int(input())
data = []
for index in range(size):
    data.append(list(input().rstrip().split()))
    data[index][1] = int(data[index][1])

result = SortTheArray(array=data).sort_by_name()

for _data in result:
    print('{} {}'.format(_data[0], _data[1]))
