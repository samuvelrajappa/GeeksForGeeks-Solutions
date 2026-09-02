''' Structure of Binary Tree Node
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def maxDiff(self, root):
        # code here
        # Initialize the maximum difference to a very small number
        self.max_difference = -float('inf')

        def dfs(node):
            if not node:
                return float('inf')

            # Leaf nodes have no descendants to compute a difference with
            if not node.left and not node.right:
                return node.data

            # Get the minimum value from the left and right subtrees
            left_min = dfs(node.left)
            right_min = dfs(node.right)

            # The smallest descendant value available for the current node
            min_descendant = min(left_min, right_min)

            # Update the global maximum difference (Ancestor - Descendant)
            self.max_difference = max(self.max_difference, node.data - min_descendant)

            # Return the minimum value in this entire subtree to the parent
            return min(node.data, min_descendant)

        dfs(root)
        return self.max_difference