import heapq 
class Solution:
    def totalCost(self, costs, k: int, candidates: int) -> int:
        answer = 0
        costs_len = len(costs)
        if costs_len <= candidates:
            costs.sort()
            answer = sum(costs[:k])
            return answer
        first_index , second_index = 0,1
        if len(costs) > 2*candidates:
            first_half = costs[:candidates]
            second_half = costs[-candidates:]
            remaining = costs[candidates:-candidates]
        else :
            first_half = costs[:candidates]
            second_half = costs[candidates:]
            remaining = []
        heapq.heapify(first_half)
        heapq.heapify(second_half)
        for i in range(k):
            first_min =  heapq.heappop(first_half)
            try:
                second_min = heapq.heappop(second_half)
            except:
                for j in range(k-i):
                    answer += first_min
                    first_min = heapq.heappop(first_half)
                return answer
            if first_min>second_min:
                answer += second_min
                heapq.heappush(first_half,first_min)
                if first_index+second_index<=len(remaining) > 0: 
                    heapq.heappush(second_half,remaining[-second_index])
                    second_index += 1 
            else:
                answer += first_min
                heapq.heappush(second_half,second_min)
                if first_index+second_index<=len(remaining) > 0: 
                    heapq.heappush(first_half,remaining[first_index])
                    first_index +=1
        return answer
Results = Solution().totalCost([17,12,10,2,7,2,11,20,8],3,4) # 11
print(Results)