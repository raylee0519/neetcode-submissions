class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {
            ")" : "(",
            "}" : "{",
            "]" : "[",
        }
        for i in s :
            if i in "({[" : stack.append(i)
            else :
                if not stack : stack.append(i)
                if pair[i] == stack[-1] :
                    stack.pop()
                else : return False
        if not stack : return True
        else : return False