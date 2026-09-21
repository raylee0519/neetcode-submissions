class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mN, mX = 1, max(piles)
        count = 0
        while mN < mX :
            mid = (mN + mX) // 2
            for i in piles :
                count += (i // mid)
                if i % mid != 0 :
                    count += 1
            if count <= h :
                mX = mid
            else :
                mN = mid + 1
            count = 0
        return mN