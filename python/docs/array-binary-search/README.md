# Binary Search of Sorted Array
Write a function called binary_search which takes in 2 parameters: a sorted array and the search key. Without utilizing any of the built-in methods available to your language, return the index of the array’s element that is equal to the value of the search key, or -1 if the element is not in the array.

## Whiteboard Process
![](/binary_search.png)

## Approach & Efficiency
I took the approach of having a shifting search window that halves in size on each iteration of the while loop. On each iteration, the value at the midpoint of the search window is checked against the target value and if they are equivalent, the midpoint index is returned.
Otherwise, the search window halves in size and the search continues. If the two pointers holding the high and low indexes of the search window without finding the target, the while loop exits and the algo returns -1.

### Big O

- **Time**: **O(log(n))** Since the search window halves on each iteration, this algo runs on logarithmic time. The max number of iterations to find the target is proportional to the base 2 logarithm of the input length.
- **Space**: **O(1)** Since only three pointer variables are needed regardless of input size, the space complexity is constant.
