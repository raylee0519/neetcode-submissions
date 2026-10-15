class Solution:
    def firstUniqChar(self, s: str) -> int:
        dup = {}
        for i in range(len(s)) :
            dup[s[i]] = dup.get(s[i], 0) + 1
        for i in range(len(s)) :
            number = dup.get(s[i])
            if number == 1 :
                return i
        return -1