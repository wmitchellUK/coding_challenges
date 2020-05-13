Write a function to see if a binary tree ↴ is "superbalanced" (a new tree property we just made up).
A tree is "superbalanced" if the difference between the depths of any two leaf nodes ↴ is no greater than one.

Here's a sample binary tree node class:

  class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right
 
Sometimes it's good to start by rephrasing or "simplifying" the problem.

The requirement of "the difference between the depths of any two leaf nodes is no greater than 1" implies that we'll have to compare the depths of `all possible pairs` of leaves. That'd be expensive—if there are 
n leaves, there are O(n2)possible pairs of leaves.

But we can simplify this requirement to require less work. For example, we could equivalently say:

"The difference between the min leaf depth and the max leaf depth is 1 or less"
"There are at most two distinct leaf depths, and they are at most 1 apart"
