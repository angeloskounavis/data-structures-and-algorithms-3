# Challenge Summary
Add a new method to the linked list class that returns the kth value from the end of a linked list.


## Whiteboard Process
[](linked-list-kth.png)

## Approach & Efficiency
- This method require list traversal and creating a new python list from the values of the linked list
- It uses python list negative indexing to return the kth value from the end of the list (-1 - k)

### Efficiency
- Method is O(n) for TIME because they require traversing the list
- Methods are O(n) for SPACE since it creates a python list of equal length to the linked list

## Solution

```python
# Assume a linked list like this exists: head -> (1) -> (2) -> (3) None
example_list.kth_from_end(1)

# it should return 2 which is at the index of -2 in the new list (one away from the end at index -1)

```

