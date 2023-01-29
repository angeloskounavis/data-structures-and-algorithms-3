# Hashtables
Hashtables are a data structure that allow for O(1) read times of key-value elements. They rely on a hashing algorithm / function to transform a given key into an index for the hash tables buckets.

## Challenge

Implement a hash table from scratch in python.

## Approach & Efficiency

Space - O(n) - amount of memory used is related to the number of inputs.
Time: Depends on the operation.
- Read -> O(1) due to the hashed keys.
- Write -> O(1) - hashing algorithm should always take same time to run.


## API

**set**
Arguments: key, value
Returns: nothing
This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
Should a given key already exist, replace its value from the value argument given to this method.

**get**
Arguments: key
Returns: Value associated with that key in the table

**has**
Arguments: key
Returns: Boolean, indicating if the key exists in the table already.

**keys**
Returns: Collection of keys

**hash**
Arguments: key
Returns: Index in the collection for that key
