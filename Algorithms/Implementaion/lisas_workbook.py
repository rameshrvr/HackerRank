

def find_special_prblems(array, prob_per_page):
    page_no = 1
    special_problems = 0
    for probs in array:
        if probs % prob_per_page == 0:
            total_pages = (probs / prob_per_page)
        else:
            total_pages = (probs / prob_per_page) + 1

        for x in range(0, total_pages):
            _start = (x * prob_per_page) + 1
            if (_start + (prob_per_page - 1)) <= probs:
                _end = _start + (prob_per_page - 1)
            else:
                _end = probs
            if _start <= page_no <= _end:
                special_problems += 1
            page_no += 1

    return special_problems


my_input = map(int, raw_input().rstrip().split(' '))
array = map(int, raw_input().rstrip().split(' '))

print find_special_prblems(
    array=array, prob_per_page=my_input[1]
)
