# Complete the whatFlavors function below.
def whatFlavors(cost, money) -> tuple:

    hash = dict()
    for idx, c in enumerate(cost):
        hash[c] = idx

    for idx, c in enumerate(cost):
        pair = money - c
        if pair in hash:
            if idx != hash[pair]:
                return idx, hash[pair]


t = int(input())
for _ in range(t):
    money = int(input())
    _ = int(input())
    arr = list(map(int, input().rstrip().split()))
    i, j = whatFlavors(arr, money)
    print(i + 1, end=" ")
    print(j + 1)
