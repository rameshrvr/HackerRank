
def operate_sequence(query, x, y, last_answer):
    if query == 1:
        seq = get_seqlist_number(
            last_answer=last_answer, x=x
        )
        SEQUENCES[seq].append(y)
        return None
    else:
        seq = get_seqlist_number(
            last_answer=last_answer, x=x
        )
        seq_size = len(SEQUENCES[seq])
        return SEQUENCES[seq][y % seq_size]


def get_seqlist_number(last_answer, x):
    return (x ^ last_answer) % N


##################
details = list(map(int, input().split()))
N, Q = details[0], details[1]

SEQUENCES = [[] for _ in range(N)]
LAST_ANS = 0

for _ in range(Q):
    query_data = list(map(int, input().split()))
    temp = operate_sequence(
        query=query_data[0], x=query_data[1], y=query_data[2],
        last_answer=LAST_ANS
    )
    if temp is not None:
        LAST_ANS = temp
        print(LAST_ANS)
##################
