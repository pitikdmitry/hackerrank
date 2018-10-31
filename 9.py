def count_deletions(text: str) -> int:
    counter = 0

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            counter += 1

    return counter


q = int(input())
for _ in range(q):
    text = input()
    print(count_deletions(text))
