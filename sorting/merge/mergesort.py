def mergesort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = n // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    i = 0
    j = 0
    arr = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1

    if i == len(left):
        arr.extend(right[j:])
    else:
        arr.extend(left[i:])
    return arr


