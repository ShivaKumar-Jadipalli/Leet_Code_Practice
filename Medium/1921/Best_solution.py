class Solution:
    def eliminateMaximum(self, dist, speed):
        arrival = [(d-1)//s for d,s in zip(dist,speed)]
        arrival.sort()
        for i,a in enumerate(arrival):
            if i > a:
                return i
        return len(arrival)
    


print(Solution().eliminateMaximum(dist = [3, 5, 7, 4, 5], speed = [2, 3, 6, 3, 2])) # 2 
print(Solution().eliminateMaximum([4,2,8],[2,1,4])) # 2
print(Solution().eliminateMaximum([1,1,2,3],[1,1,1,1])) # 1
