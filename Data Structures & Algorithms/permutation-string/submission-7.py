class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) : return False
        s1_c, s2_c = {}, {}
        left = 0
        matched = False
        
        for i in s1 :
            s1_c[i] = s1_c.get(i, 0) + 1
        
        for right in range(len(s2)) :
            s2_c[s2[right]] = s2_c.get(s2[right],0) + 1
            if len(s1) < (right - left + 1) :
                s2_c[s2[left]] -= 1
                left += 1
            
            if len(s1) == (right - left + 1) :
                matched = True

                for i in s1_c :
                    if s1_c[i] != s2_c.get(i, 0) :
                        matched = False
                        break

                if matched :
                    return True

        return False