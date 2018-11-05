# test dynamic task


def safe_order(n: int, order: str) -> int:
    if len(order) == n:
        print(order)
        return 1

    amount = 1
    if len(order) == 0:
        amount += safe_order(n, order + 'A')
    elif order[len(order) - 1] != 'A':
        amount += safe_order(n, order + 'A')

    amount += safe_order(n, order + 'B')

    return amount


n = 3
print(safe_order(n, ''))
