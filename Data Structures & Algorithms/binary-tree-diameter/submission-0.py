class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        answer = 0

        def depth(node):
            nonlocal answer

            if not node:
                return 0

            left_depth = depth(node.left)
            right_depth = depth(node.right)

            answer = max(answer, left_depth + right_depth)

            return 1 + max(left_depth, right_depth)

        depth(root)
        return answer