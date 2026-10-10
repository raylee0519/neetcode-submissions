class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_c, t_c = {}, {}
        for i in s :
            s_c[i] = s_c.get(i, 0) + 1
        for j in t :
            t_c[j] = t_c.get(j, 0) + 1
        return s_c == t_c