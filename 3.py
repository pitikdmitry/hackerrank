# New Year Chaos
def swap(q, i, j):
    temp = q[i]
    q[i] = q[j]
    q[j] = temp
    return q


# def countBribes(q, counter, bribes):
#     need_recursion = False
#     for i in range(1, len(q)):
#         if q[i] < q[i - 1]:
#             q = swap(q, i, i - 1)
#             bribes += 1
#             counter += 1
#             need_recursion = True
#             if counter >= 3:
#                 print("Too chaotic")
#                 return
#         else:
#             counter = 0
#
#     if need_recursion:
#         return countBribes(q, 0, bribes)
#     else:
#         print(bribes)
#         return bribes


def countBribes(q, counter, bribes):
    # need_recursion = False
    for i in range(1, len(q)):
        if q[i] < q[i - 1]:
            q = swap(q, i, i - 1)
            bribes += 1
            counter += 1
            i = 0
            # need_recursion = True
            if counter >= 3:
                print("Too chaotic")
                return
        else:
            counter = 0

    # if need_recursion:
    #     return countBribes(q, 0, bribes)
    # else:
    #     print(bribes)
    #     return bribes


def minimumBribes(q: []):
    counter = 0
    bribes = 0
    countBribes(q, counter, bribes)


t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    bribes = minimumBribes(arr)
