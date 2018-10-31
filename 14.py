def minimumAbsoluteDifference(arr: []) -> int:
    arr = sorted(arr)
    min = None
    for i in range(1, len(arr)):
        new_min = abs(arr[i - 1] - arr[i])

        if min is None:
            min = new_min
        else:
            if new_min < min:
                min = new_min
    return min


n = int(input())
arr = list(map(int, input().rstrip().split()))
print(minimumAbsoluteDifference(arr))
