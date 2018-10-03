# Hash Tables: Ransom Note
n, m = map(int, input().split())

magazine = input().split()
note = input().split()

words = {}
for word in magazine:
    if word not in words:
        words[word] = 1
    else:
        words[word] += 1

error = False

for word in note:
    if word not in words:
        error = True
        print('No')
        break
    elif words[word] < 1:
        error = True
        print('No')
        break
    else:
        words[word] -= 1

if not error:
    print('Yes')
