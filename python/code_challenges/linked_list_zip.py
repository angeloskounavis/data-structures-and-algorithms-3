from data_structures.linked_list import LinkedList, Node


def zip_lists(a, b):
    """
    Zip two linked lists together, always starting with list a.
    """
    # handles an empty input list
    if not a.head or not b.head:
        return LinkedList(a.head) if a.head else LinkedList(b.head)

    # makes a dummy pointer for the head of the new ll, also makes a cur variable starting at list a head
    dummy = cur = a.head
    a.head = a.head.next
    # makes a flag to allow for alternating the lists for zipping
    even = False

    # happy path

    while a.head and b.head:
        if not even:
            cur.next = b.head
            b.head = b.head.next
            even = True
        else:
            cur.next = a.head
            a.head = a.head.next
            even = False
        cur = cur.next
    # once the tail has been reached for one list, this should point the new list to whichever list still has values
    cur.next = a.head or b.head
    # est a new LL instance and set its head to our dummy
    return LinkedList(dummy)



