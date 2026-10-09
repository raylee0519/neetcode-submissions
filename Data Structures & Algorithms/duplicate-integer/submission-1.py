class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = []
        for i in nums :
            if i in result : return True
            result.append(i)
        return False