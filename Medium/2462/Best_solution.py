import heapq 
class Solution():        
    def totalCost(self,costs, k: int, candidates: int) -> int:
        n=len(costs)
        if candidates*2+k>n:
            return sum(sorted(costs)[:k])
        first=costs[:candidates]
        second=costs[-candidates:]
        i,j=candidates,n-1-candidates
        heapq.heapify(first)
        heapq.heapify(second)
        ans=0
        for _ in range(k):
            if first[0]<=second[0]:
                ans+=heapq.heapreplace(first,costs[i])
                i+=1
            else:
                ans+=heapq.heapreplace(second,costs[j])
                j-=1
        return ans
print(Solution().totalCost([3,2,1,1,2,3],5,3))  # Expected output: 423
