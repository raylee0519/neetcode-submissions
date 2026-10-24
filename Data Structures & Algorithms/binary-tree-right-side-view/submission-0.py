from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([root])
        answer = []

        while q:
            length = len(q)

            for i in range(length):
                node = q.popleft()

                if i == length - 1:
                    answer.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        return answer