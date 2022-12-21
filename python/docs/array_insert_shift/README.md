# Insert to Middle of an Array
Write a function called `insert_shift_array` which takes in an array and a value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.

## Whiteboard Process
![](/insert_shift_array.png)

## Approach & Efficiency
- I calculated the midpoint of the array by dividing its length by 2.
  - I round the result up to account for array with odd-numbered length.
- Next I used the `insert()` method to put the new value at the calculated midpoint of a new array.

### Big O
- Time -> O(n) because the number of elements that have to be shifted to fit the new value scales linearly with the size of the input.
- Space -> O(n) because a new array of length n + 1 is created.
