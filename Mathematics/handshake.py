

def find_no_of_handshakes(n):
    # Formula for No of handshakes would be nCr
    # Here n = input and r = 2. So nC2
    # nC2 = (n * (n - 1)) / 2
    return int((n * (n - 1)) / 2)


##################
testcases = int(input())
for _ in range(testcases):
    data = int(input())
    print(find_no_of_handshakes(n=data))
##################
