# Singly Linked List
A linked list is a data structure alternative to using arrays. Linked lists (LLs) consist of nodes - each node holds a value and a pointer to the next node in the list. Depending on your requirements, a LL may be more appropriate than an array because you are able to add to and delete from the beginning of the list in constant time. Also, LLs do not require a contiguous block of memory.

## Challenge
The challenge is to create an implementation of the LL data structure.
This necessitates creating both a Node and LinkedList class.
Furthermore, the LL must have the ability to insert new nodes at the beginning, search the list to see if it includes values, and print a string representation of the list.

## Approach & Efficiency
For the insert function, I took the classic approach of inserting at the beginning - this takes constant time.
The includes function takes linear time to search for a value because it must traverse potentially the whole list.
For the string representation of the collection of values, if this is the first time printing it or if it is not up-to-date, this operation takes linear time. Otherwise, if the collection exists and is up-to-date, it takes constant time.


## API
- insert(): Inserts a new node at the beginning of the list and sets head to this node.
- includes(): Checks if a target value is included amongst the node values held in the list.
- __str__(): Returns a string representation of the values in then LL. **NOTE - I used the existing special function name instead of 'to string'**
