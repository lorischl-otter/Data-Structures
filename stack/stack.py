"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.

1. Implement the Stack class using an array as the underlying storage
    structure. Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Stack?

    The main difference with using a linked list was that both adding and
    removing values needed to be pointed at the tail of the linked list,
    rather than just using indexing or appending.

"""
from singly_linked_list import LinkedList
# Second implementation, with singly linked lists:


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size > 0:
            val = self.storage.tail.get_value()
            self.storage.remove_tail()
            self.size -= 1
            return val
        else:
            return None


# # First implementation -- all tests pass.
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.storage.append(value)
#         self.size += 1

#     def pop(self):
#         if self.size > 0:
#             val = self.storage[-1]
#             del self.storage[-1]
#             self.size -= 1
#             return val
#         else:
#             return None
