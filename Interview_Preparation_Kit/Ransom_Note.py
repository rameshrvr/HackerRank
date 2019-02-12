

def check_magazine_has_word(magazine, note):
    for word in note:
        if magazine.get(word):
            magazine[word] -= 1
        else:
            return 'No'
    return 'Yes'


test_details = list(map(int, input().rstrip().split()))
_magazine = input().rstrip().split()
magazine = {}
for key in _magazine:
    if magazine.get(key):
        magazine[key] += 1
    else:
        magazine[key] = 1
note = input().rstrip().split()


print(check_magazine_has_word(magazine, note))
