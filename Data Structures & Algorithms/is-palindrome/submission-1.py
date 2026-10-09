class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = []
        for i in s :
            if i.isalnum() == True : result.append(i.lower())
        return result == result[::-1]