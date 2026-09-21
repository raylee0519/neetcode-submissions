class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = dict()
        max_word = 0
        result = 0
        left = 0
        for right in range(len(s)) :
            counter[s[right]] = counter.get(s[right], 0) + 1
            max_word = max(max_word, counter[s[right]])
            if int(right - left + 1) - max_word > k :
                counter[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result