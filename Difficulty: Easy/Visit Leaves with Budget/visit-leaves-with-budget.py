''' Binary Tree Node Structure
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def getCount(self, root, k):
        # code here
        # List to store the levels of all leaf nodes
                leaf_levels = []

                # Helper function to traverse the tree using DFS
                def dfs(node, level):
                    if not node:
                        return

                    # Check if current node is a leaf node
                    if not node.left and not node.right:
                        leaf_levels.append(level)
                        return

                    # Traverse left and right subtrees increasing the level
                    dfs(node.left, level + 1)
                    dfs(node.right, level + 1)

                # Start DFS traversal from the root at level 1
                dfs(root, 1)

                # Sort the leaf levels to greedily pick the cheapest ones
                leaf_levels.sort()

                count = 0
                total_cost = 0

                # Visit leaves within the budget
                for cost in leaf_levels:
                    if total_cost + cost <= k:
                        total_cost += cost
                        count += 1
                    else:
                        break

                return count