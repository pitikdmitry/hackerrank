str1 = input()
str2 = input()

counter = 0
common = {}
for c in str1:
    if c not in str2:
        counter += 1
    else:
        if c in common:
            common[c] += 1
        else:
            common[c] = 1


for c in str2:
    if c not in str1:
        counter += 1
    else:
        if c in common and common[c] > 0:
            common[c] -= 1
        else:
            counter += 1


for key, value in common.items():
    if value > 0:
        counter += value

print(counter)
