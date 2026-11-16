class Solution:
    def isValid(self, s: str) -> bool:
        if not s : return True
        match = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        stack = []
        for i in s :
            if i in "[{(" :
                stack.append(i)
            else :
                if not stack : return False
                if match[i] == stack[-1] :
                    stack.pop()
                else : return False
        return stack == []