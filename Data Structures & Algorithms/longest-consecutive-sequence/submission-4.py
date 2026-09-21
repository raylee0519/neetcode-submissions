class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        re_set = set(nums)
        answer = 0 

        for i in re_set :
            if i - 1 not in re_set :
                current = i
                length = 1

                while current + 1 in re_set :
                    current += 1
                    length += 1
                
                answer = max(length, answer)
        
        return answer