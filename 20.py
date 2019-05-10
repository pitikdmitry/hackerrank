# create array of common elements from array1 and array2


def same_elements(arr_1: [], arr_2: []) -> []:
    i, j = 0, 0
    res = []
    while i < len(arr_1) and j < len(arr_2):
        if arr_1[i] == arr_2[j]:
            res.append(arr_1[i])
            i += 1
            j += 1
        elif arr_1[i] > arr_2[j]:
            j += 1
        else:
            i += 1

    return res


arr_1 = [1, 2, 3, 4, 5]
arr_2 = [2, 4]

print(same_elements(arr_1, arr_2))
