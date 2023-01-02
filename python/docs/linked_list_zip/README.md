# Stacks and Queues

Implemented the stack and queue data structures (DSs). These two DSs are based on the same types of nodes that are used in
a linked list. A stack is a DS which follows last-in-first-out for addition and removal of nodes and has only top attribute. A queue is a DS which follows first-in-first-out and knows about both its front and rear nodes.

## Challenge

For the above DSs implement methods for the following actions:

- Node addition (push and enqueue)
- Node removal (pop and dequeue)
- Peeking the top or front nodes
- Checking if the DS is empty

## Approach & Efficiency

The efficiency of all methods implemented so far is O(n) for both time and space due to the use of the top / front / rear attributes.

## API

### Stack

**push**
Arguments: value
adds a new node with that value to the top of the stack with an O(1) Time performance.

**pop**
Arguments: none
Returns: the value from node from the top of the stack
Removes the node from the top of the stack
Should raise exception when called on empty stack

**peek**
Arguments: none
Returns: Value of the node located at the top of the stack
Should raise exception when called on empty stack

**is empty**
Arguments: none
Returns: Boolean indicating whether or not the stack is empty.

### Queue

**enqueue**
Arguments: value
adds a new node with that value to the back of the queue with an O(1) Time performance.

**dequeue**
Arguments: none
Returns: the value from node from the front of the queue
Removes the node from the front of the queue
Should raise exception when called on empty queue

**peek**
Arguments: none
Returns: Value of the node located at the front of the queue
Should raise exception when called on empty stack

**is empty**
Arguments: none
Returns: Boolean indicating whether or not the queue is empty
