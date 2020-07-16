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
        current = self.right
        # traverse to the farthest right node
        while current:
            max_value = current.value
            current = current.right
        return max_value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
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

        # fn(self.left), for_each(self.left, fn) if self.left is not None
        # # call fn & for_each on non-empty right
        # fn(self.right), for_each(self.right, fn) if self.right is not None

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


# breakpoint()
