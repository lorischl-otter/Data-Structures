"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if target equals root value, return true
        if target == self.value:
            return True
        # else, check value of target to follow right or left nodes
        else:
            # mimic structure of insert to find where value would be
            if target < self.value:
                # if target is less than parent,
                # but left node is empty, return False
                if self.left is None:
                    return False
                # otherwise, continue recursively w/ left node
                else:
                    return self.left.contains(target)
            # if target is larger than root/parent, go to right node
            else:
                if self.right is None:
                    return False
                else:
                    return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # set initial max value based on root
        max_value = self.value
        # move to higher value to the right
        current = self.right  # or current = self
        # traverse to the farthest right node
        while current:  # or while current is not None
            max_value = current.value
            current = current.right
        return max_value

    # better iterative in class
    # def get_max(self)
    #     current = self
    #     while current.right is not None:
    #         current = current.right
    #     return current.value

    # Recursive solution covered in lecture
    # def get_max(self):
    #     if not self.right:
    #         return self.value
    #     return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # depth-first traversal
        # call fn on root / current value
        fn(self.value)
        # call for_each on non-empty left
        if self.left is None:
            pass
        else:
            self.left.for_each(fn)
        # call for_each on non-empty right
        if self.right is None:
            pass
        else:
            self.right.for_each(fn)

    # better recursive iteration in class
    # this is an example of depth-first traversal
    # def for_each(self, fn):
    #     fn(self.value)
    #     if self.left:
    #         self.left.for_each(fn)
    #     if self.right:
    #         self.right.for_each(fn)

    def iterative_breadth_first_for_each(self, fn):
        from collections import dequeue
        # BFT: FIFO traversal
        # we'll use a queue structure to facilitate ordering
        # pattern the same as before, except using a queue
        queue = dequeue()
        queue.append(self)

        while len(queue) > 0:
            current = queue.popleft()  # equivalent of dequeueing
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            fn(current.value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        # create an empty list
        all_values = []
        # create an appending function
        fn = lambda x: all_values.append(x)
        # us the for each method to get all numbers into a list
        self.for_each(fn)
        # print the sorted list
        all_values = sorted(all_values)
        for value in all_values:
            print(value)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        from collections import deque
        queue = deque()
        queue.append(node)
        while len(queue) > 0:
            current = queue.popleft()
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            print(current.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = []
        stack.append(node)
        while len(stack) > 0:
            current = stack.pop()
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
            print(current.value)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        # same implementation as in_order_print, without sorting values
        all_values = []
        fn = lambda x: all_values.append(x)
        self.for_each(fn)
        for value in all_values:
            print(value)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        # modify implementation of for_each, to be post_order
        all_values = []
        if self.left:
            self.left.post_order_dft(node)
        if self.right:
            self.right.post_order_dft(node)
        all_values.append(self.value)
        for value in all_values:
            print(value)

# breakpoint()
