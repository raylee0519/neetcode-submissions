class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_c, t_c = dict(), dict()
        for i in s :
            s_c[i] = s_c.get(i,0) + 1
        for i in t :
            t_c[i] = t_c.get(i,0) + 1
        return s_c == t_c