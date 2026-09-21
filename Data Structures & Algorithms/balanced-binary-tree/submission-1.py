class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def dfs(node):
            if not node:
                return 0

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            if abs(left_depth - right_depth) > 1:
                self.balanced = False

            return 1 + max(left_depth, right_depth)

        dfs(root)
        return self.balanced