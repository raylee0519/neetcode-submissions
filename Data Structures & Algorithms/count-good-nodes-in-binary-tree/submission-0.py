# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def isGood(root, value) :
            count = 0
            if root.val >= value :
                value = root.val
                count += 1
            if root.left :
                left = isGood(root.left ,value)
                count += left
            if root.right :
                right = isGood(root.right, value)
                count += right
            return count
        return isGood(root, float("-inf"))