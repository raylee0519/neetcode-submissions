# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def find(root) :
            if not root :
                return False
            if find_sub(root, subRoot) :
                return True
            return find(root.left) or find(root.right)


        def find_sub(root, subroot) :
            if not root and not subroot :
                return True
            if not root or not subroot :
                return False
            if root.val != subroot.val :
                return False
    
            return find_sub(root.left, subroot.left) and find_sub(root.right, subroot.right)

        return find(root)