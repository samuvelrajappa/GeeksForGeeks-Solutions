class Solution:
    def absDiff(self, root):
        self.prev = None
        self.min_diff = float('inf')

        def inorder(node):
            if not node:
                return

            # 1. Traverse the left subtree
            inorder(node.left)

            # 2. Process current node
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.data - self.prev)
            self.prev = node.data

            # 3. Traverse the right subtree
            inorder(node.right)

        inorder(root)
        return self.min_diff
