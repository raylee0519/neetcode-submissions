class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left = 0
        right = 0
        result = 0

        while right < len(s):
            if s[right] in window:
                window.remove(s[left])
                left += 1
            else:
                window.add(s[right])
                result = max(result, right - left + 1)
                right += 1

        return result