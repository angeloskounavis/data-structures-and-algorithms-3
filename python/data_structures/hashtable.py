from data_structures.linked_list import LinkedList, Node

# **set**
# Arguments: key, value
# Returns: nothing
# This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
# Should a given key already exist, replace its value from the value argument given to this method.
#
# **get**
# Arguments: key
# Returns: Value associated with that key in the table
#
# **has**
# Arguments: key
# Returns: Boolean, indicating if the key exists in the table already.
#
# **keys**
# Returns: Collection of keys
#
# **hash**
# Arguments: key
# Returns: Index in the collection for that key


class Hashtable:
    """
    Implements a hash table in python.
    """

    def __init__(self, size=1024):
        self.size = size
        self._buckets = [None] * size

    def set(self, key, value):
        index = self.hash(key)
        if self._buckets[index] is None:
            self._buckets[index] = LinkedList()
            self._buckets[index].insert([key, value])
        else:
            self._buckets[index].insert([key, value])

    def get(self, key):
        index = self.hash(key)
        if self._buckets[index] is not None:
            return self._buckets[index].get(key)
        else:
            return None

    def has(self, key):
        return True if self.get(key) else False

    def keys(self):
        key_list = []
        for item in self._buckets:
            if item is not None:
                current = item.head
                while current:
                    key_list.append(current.value[0])
                    current = current.next
        return key_list

    def hash(self, key):
        return hash(key) % self.size

