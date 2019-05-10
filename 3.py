def generate_parenthesis(n, arr) -> None:
    if n == len(arr):
        print(arr)
    else:
        arr.append('(')
        generate_parenthesis(n, arr)
        arr.pop()

        arr.append(')')
        generate_parenthesis(n, arr)
        arr.pop()


arr = []
n = 4
generate_parenthesis(n, arr)
