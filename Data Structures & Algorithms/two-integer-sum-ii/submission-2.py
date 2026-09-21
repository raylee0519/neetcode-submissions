class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a, b = 0, len(numbers) - 1
        while a < b :
            answer = numbers[a] + numbers[b]
            if answer == target : break
            if answer > target :
                b -= 1
            else :
                a += 1
        return [a+1, b+1]