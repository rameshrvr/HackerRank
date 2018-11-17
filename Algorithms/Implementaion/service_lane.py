

def calc_minimum_vehicle_size(array, test_input):
    return min(array[test_input[0]:(test_input[1] + 1)])


#################
testcase_details = map(int, raw_input().strip().split())
array = map(int, raw_input().strip().split())
inputs = []
for _ in xrange(testcase_details[1]):
    inputs.append(map(int, raw_input().strip().split()))

for test_input in inputs:
    print calc_minimum_vehicle_size(array, test_input)
#################
