''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def numberOfTurns(self, root, p, q):
        # code here
        def findPath(node, key, path):
            if not node:
                return False
            if node.data == key:
                return True
            
            # Try traversing left
            path.append('L')
            if findPath(node.left, key, path):
                return True
            path.pop()
            
            # Try traversing right
            path.append('R')
            if findPath(node.right, key, path):
                return True
            path.pop()
            
            return False

        path_p = []
        path_q = []
        
        # Get paths from root to both nodes
        findPath(root, p, path_p)
        findPath(root, q, path_q)
        
        # Find the length of the common prefix (path from root to LCA)
        i = 0
        while i < len(path_p) and i < len(path_q) and path_p[i] == path_q[i]:
            i += 1
            
        # Get the relative paths from the LCA downwards
        sub_p = path_p[i:]
        sub_q = path_q[i:]
        
        # Helper function to count turns (transitions between 'L' and 'R')
        def countTurnsInPath(path):
            turns = 0
            for k in range(1, len(path)):
                if path[k] != path[k-1]:
                    turns += 1
            return turns

        # Case 1: p is the LCA (path goes straight down from p to q)
        if len(sub_p) == 0:
            turns = countTurnsInPath(sub_q)
            return turns if turns > 0 else -1
            
        # Case 2: q is the LCA (path goes straight up from p to q)
        if len(sub_q) == 0:
            turns = countTurnsInPath(sub_p)
            return turns if turns > 0 else -1
            
        # Case 3: LCA is an intermediate node above both p and q
        turns_p = countTurnsInPath(sub_p)
        turns_q = countTurnsInPath(sub_q)
        
        # Total turns = turns in p's branch + turns in q's branch + 1 turn at the LCA
        total_turns = turns_p + turns_q + 1
        return total_turns