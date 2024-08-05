class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = 0
        original = x
        while x > 0:
            s += x % 10
            x //=10
        if original % s == 0:
            return s
        return -1
    
    
print(Solution().sumOfTheDigitsOfHarshadNumber(5)) 