"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def set_next(self, new_next):
        self.next = new_next

    def set_prev(self, new_prev):
        self.prev = new_prev


"""
Our doubly-linked list class. It holds references to
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        new_prev = self.head
        if self.head is None and self. tail is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.head.set_prev(new_node)
            new_node.set_next(new_prev)
            self.head = new_node
            self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # can be refactored to 3 lines
        # can use delete method 
        # remove conditionals -- those can all be included in delete
        val = self.head.value
        if self.head is None:
            return
        if not self.head.next:
            self.head = None
            self.tail = None
            self.length -= 1
            return val
        self.head = self.head.next
        self.head.set_prev(None)
        self.length -= 1
        return val

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        new_prev = self.tail
        if self.tail is None and self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.tail.set_next(new_node)
            new_node.set_prev(new_prev)
            self.tail = new_node
            self.length += 1

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        val = self.tail.value
        if self.tail is None:
            return
        if not self.tail.prev:
            self.tail = None
            self.head = None
            self.length -= 1
            return val
        self.tail = self.tail.prev
        self.tail.set_next(None)
        self.length -= 1
        return val

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        self.add_to_head(node.value)
        self.delete(node)

    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        self.add_to_tail(node.value)
        self.delete(node)

    """
    Deletes the input node from the List, preserving the
    order of the other elements of the List.
    """
    def delete(self, node):
        # can use if statements for particular nodes
        # i.e. if node is head / tail
        if self.tail is None and self.head is None:
            return None
        elif not node.next:
            self.remove_from_tail()
        elif not node.prev:
            self.remove_from_head()
        else:
            node.next.set_prev(node.prev)
            node.prev.set_next(node.next)
            self.length -= 1

    """
    Finds and returns the maximum value of all the nodes
    in the List.
    """
    def get_max(self):
        if not self.head:
            return None
        max_value = self.head.value
        current = self.head.next
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value

# breakpoint()
