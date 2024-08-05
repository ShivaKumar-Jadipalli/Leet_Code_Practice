class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        x_sum=0
        for i in str(x):
            x_sum+=int(i)
        if x%x_sum==0:
            return x_sum
        return -1 
print(Solution().sumOfTheDigitsOfHarshadNumber(23)) 
print(Solution().sumOfTheDigitsOfHarshadNumber(18)) 