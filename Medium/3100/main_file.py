class Solution:
    def maxBottlesDrunk(self, numBottles, numExchange):
        answer = 0
        while numBottles >= numExchange:
            numBottles -= numExchange 
            answer += numExchange
            numExchange +=1 
            numBottles += 1
        answer += numBottles
        return answer
result = Solution().maxBottlesDrunk(13,6)
print(result)
result = Solution().maxBottlesDrunk(10,3)
print(result)