# Complete the countSwaps function below.
def countSwaps(arr):
    swaps = 0
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]:
                swaps += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print("Array is sorted in " + str(swaps) + " swaps.")
    print("First Element: " + str(arr[0]))
    print("Last Element: " + str(arr[len(arr) - 1]))


n = int(input())
arr = list(map(int, input().split()))
countSwaps(arr)
