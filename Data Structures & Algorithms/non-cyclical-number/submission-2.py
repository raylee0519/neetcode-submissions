class Solution:
    def isHappy(self, n: int) -> bool:
        dup = set()
        num = self.getDigit(n)
        while num not in dup :
            if num == 1 :
                return True
            dup.add(num)
            num = self.getDigit(num)
        return False

    def getDigit(self, n) :
        total = 0
        for digit in str(n) :
            total += int(digit) ** 2
        return total