class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right :
            mid = (left + right) // 2
            hours = 0
            for i in piles :
                hours += (i // mid)
                if i % mid != 0 : hours += 1
            
            if hours <= h :
                right = mid
            else :
                left = mid + 1
        return left