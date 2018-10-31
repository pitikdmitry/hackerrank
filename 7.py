# Complete the freqQuery function below.
def freqQuery(queries):
    d = {}
    counters = {}
    for query in queries:
        op = query[0]
        val = query[1]
        if op == 1:
            if val not in d:
                d[val] = 1
            else:
                counters[d[val]] -= 1
                d[val] += 1

            if d[val] not in counters:
                counters[d[val]] = 1
            else:
                counters[d[val]] += 1
        elif op == 2:
            if val in d and d[val] >= 1:
                counters[d[val]] -= 1

                d[val] -= 1
                if d[val] not in counters:
                    counters[d[val]] = 1
                else:
                    counters[d[val]] += 1

        elif op == 3:
            done = False

            if val in counters and counters[val] > 0:
                print(1)
            else:
                print(0)


q = int(input())
queries = []

for i in range(q):
    query = list(map(int, input().split()))
    queries.append(query)

freqQuery(queries)
