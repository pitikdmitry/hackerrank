# Arrays: Left Rotation
def rotRight(arr: [], d: int) -> []:
    for i in range(d):
        last_el = arr[len(arr) - 1]
        for i in range(len(arr) - 2, -1, -1):
            arr[i + 1] = arr[i]
        arr[0] = last_el
    return arr


def rotLeft(arr: [], d: int) -> []:
    result = []
    for i in range(d, len(arr)):
        result.append(arr[i])
    for i in range(0, d):
        result.append(arr[i])
    return result


n = int(input())
d = int(input())
arr = list(map(int, input().split()))
print(rotLeft(arr, d))
