import heapq
from math import ceil
class Solution:
    def eliminateMaximum(self, dist, speed):
        gun_rounds = []
        answer =0
        for i,j in zip(dist, speed):
            gun_rounds.append(ceil(i/j))
        heapq.heapify(gun_rounds)
        for i in range(len(gun_rounds)):
            monster = heapq.heappop(gun_rounds)
            if monster > answer:
                answer += 1
            else:
                return answer
        return answer
    
print(Solution().eliminateMaximum(dist = [3, 5, 7, 4, 5], speed = [2, 3, 6, 3, 2])) # 2 
print(Solution().eliminateMaximum([4,2,8],[2,1,4])) # 2
print(Solution().eliminateMaximum([1,1,2,3],[1,1,1,1])) # 1
