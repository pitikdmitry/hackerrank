# Complete the activityNotifications function below.
def create_array(maximum: int) -> []:
    arr = []
    for i in range(maximum + 1):
        arr.append(0)
    return arr


def median_count(arr: [], d: int) -> int:

    maximum = max(arr)
    amount_array = create_array(maximum)
    for val in arr:
        amount_array[val] += 1

    counter = 0

    median_index = d // 2 + 1

    for idx, amount in enumerate(amount_array):
        counter += amount
        if counter >= median_index:
            return idx


def activityNotifications(expenditure: [], d: int) -> int:
    if len(expenditure) <= d:
        return 0

    # expenditure = sorted(expenditure)
    notifications = 0

    for i in range(d, len(expenditure)):
        median = median_count(expenditure[i - d:i], d)

        if expenditure[i] >= median * 2:
            notifications += 1

    return notifications


n, d = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
print(activityNotifications(arr, d))
