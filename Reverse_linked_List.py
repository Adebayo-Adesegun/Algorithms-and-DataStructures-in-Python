

def reverse_linked_list(head):
    """
    Reverse a linked list.

    :param head: head of the linked list
    :return: head of the reversed linked list
    """
    if head is None:
        return None

    prev = None
    curr = head
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev 