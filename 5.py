def twoStrings(first: str, second: str):
    pointer = 0
    while pointer < len(first):
        letters = pointer + 1
        while letters <= len(first):
            word = first[pointer:letters]
            res = second.find(word)
            letters += 1
            if res != -1:
                return 'YES'
        pointer += 1
    return 'NO'


q = int(input())
for q_itr in range(q):
    first = input()
    second = input()
    print(twoStrings(first, second))
