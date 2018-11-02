# Complete the maxSubsetSum function below.
def el_max_subset(arr, cur, prev):
    if cur == len(arr):
        return 0

    if cur - prev <= 1:
        return el_max_subset(arr, cur + 1, prev)
    else:
        return arr[cur] + el_max_subset(arr, cur + 1, cur)


def maxSubsetSum(arr: []) -> int:
    max = arr[0]
    for i in range(len(arr)):
        m_res = el_max_subset(arr, i, i - 2)
        if m_res > max:
            max = m_res

    return max


n = int(input())

arr = list(map(int, input().rstrip().split()))

res = maxSubsetSum(arr)

print(res)
