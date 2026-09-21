class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_c, s2_c = {}, {}

        for ch in s1:
            s1_c[ch] = s1_c.get(ch, 0) + 1

        left = 0

        for right in range(len(s2)) :
            s2_c[s2[right]] = s2_c.get(s2[right], 0) + 1
            if right - left + 1 > len(s1) :
                s2_c[s2[left]] -= 1
                left += 1

            
            if right - left + 1 == len(s1) :
                matched = True
            
                for ch in s1_c :
                    if s1_c[ch] != s2_c.get(ch, 0) :
                        matched = False
                        break
                    
                if matched :
                    return True

        return False