class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        front_nums = [1] * n
        end_nums = [1] * n

        for i in range(1, n):
            front_nums[i] = front_nums[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            end_nums[i] = end_nums[i + 1] * nums[i + 1]

        result = []

        for i in range(n):
            result.append(front_nums[i] * end_nums[i])

        return result