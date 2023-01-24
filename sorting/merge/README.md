# Blog Notes: Merge Sort

This blog will explain the merge sort implementation below line-by-line using `[8,4,23,42,16,15]` as the example input array.

```python
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
```

## Explanation

### Intro notes
The first things to note are that this is a **recursive** function and that it makes use of a **helper function** called `merge()`.

Mergesort makes use of the principle 'divide and conquer' to break down the array into the smallest possible chunks then sort and put the chunks back together recursively until the entire array is sorted.

### Mergesort - Recursive function

1. The length of the input array is set to `n`.
   - *In the first recursive call for our example, this is 6.*
2. Next the **base case** of the function is checked and if the array length is <= 1, it returns the input array.
3. The midpoint variable `mid` is set to the array length floor divided by 2.
   - *In the first recursive call for our example, this is 3*
4. The `left` and `right` variables are set the recursive call of mergesort on the values to the left and right of the `mid`point respectively.
5. Once the left and right recursive calls return for the base case, the left and right arrays are merged using the `merge` helper function.

### Merge - iterative function

1. First the index variables `i` and `j` are initialized to keep track of the current index of the left and right arrays.
2. An empty array `arr` is initialized.
3. As long as the end of one of the arrays has not been reached the comparison while loop will continue.
4. If the value at the current index of the left array is <= the value at the current index of the right array, it will be appended to the `arr` array and the left index will increment.
5. Otherwise, the value at the current right index will be appended and the right index will increment.
6. Once the end of one array (left or right) is reached, the rest of the values in the other array will be extended onto the result array.

### Visualization

![](/mergesort.png)


## Tests

- Happy path -> even length array, unique vals
- Odd length arr
- Few unique vals
- Empty array

## Efficiency

Mergesort is O(nlogn) for time and O(n) for space.
