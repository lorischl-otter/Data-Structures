"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order.

1. Implement the Queue class using an array as the underlying storage
structure. Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Queue?

   The main changes involved with the differing implementations was to ensure
   that adding to the queue translated to adding to the tail of the linked
   list, and that removing from the queue translated into removing the head
   of the linked list. (rather than using indexing/appending)

Stretch: What if you could only use instances of your Stack class to implement
the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
from singly_linked_list import LinkedList
# Second implementation, with singly linked lists:
# Queue will not be as efficient as stack, bc must use opposite ends
# did not need to use 'val' -- could have just returned the .remove_head()


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_tail(value)  # O(1)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            val = self.storage.head.get_value()  # didn't need this
            self.storage.remove_head()  # O(1) # could just return this
            self.size -= 1
            return val
        else:
            return None


# First implementation -- all tests pass.
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.storage.append(value)
#         self.size += 1

#     def dequeue(self):
#         if self.size > 0:
#             val = self.storage[0]
#             del self.storage[0]
#             self.size -= 1
#             return val
#         else:
#             return None


# Lecture implementation
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         self.storage.append(value) # O(1)
#         # self.storage.insert(0, value) # O(n)

#     def dequeue(self):
#         if len(self.storage) > 0:
#             return self.storage.pop(0) # O(n)
#             # return self.storage.pop # O(1)
