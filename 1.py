def sum_one_square(arr: [], start_i: int, start_j: int, width: int=3, height: int=3) -> int:
    summ = 0
    for i in range(start_i, start_i + width):
        for j in range(start_j, start_j + height):
            if i == start_i + 1 and (j == start_j or j == start_j + 2):
                continue
            summ += arr[i][j]
    return summ


def hourglassSum(arr: []) -> []:
    width, height = 3, 3
    if len(arr) == 0:
        return 0

    max_summ = None
    for i in range(len(arr) - width + 1):
        for j in range(len(arr[i]) - height + 1):
            square_summ = sum_one_square(arr, i, j, width, height)
            if max_summ is None:
                max_summ = square_summ
            elif square_summ > max_summ:
                max_summ = square_summ
    return max_summ


arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

result = hourglassSum(arr)
print(result)
