class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        answer = 0

        for num in num_set:
            # num이 연속 수열의 시작점인지 확인
            if num - 1 not in num_set:
                current = num
                length = 1

                while current + 1 in num_set:
                    current += 1
                    length += 1

                answer = max(answer, length)

        return answer