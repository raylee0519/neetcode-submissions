# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        def find(root) :
            nonlocal balanced
            if not root : return 0
            left = find(root.left)
            right = find(root.right)
            if abs(left - right) > 1 :
                balanced = False
            return max(left, right) + 1
        find(root)
        return balanced