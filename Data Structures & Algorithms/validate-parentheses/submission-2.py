class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        show = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for i in s :
            if i in "({[" :
                stack.append(i)
            else : 
                if not stack : return False
                if stack[-1] != show[i] : return False
                stack.pop()
        return not stack