class Solution:
    def findLatestTime(self, s: str) -> str:
        hours , minutes = s.split(":")
        hours_1, hours_2 = hours[0],hours[1]
        minutes_1,minutes_2 = minutes[0],minutes[1]
        if hours_1 =="?" and hours_2 =="?":
            hours_2,hours_1 = "1","1"
        if hours_1=="?":
            hours_1="0"
        if hours_2=="?":
            if hours_1=="1":
                hours_2 = "1"
            else:
                hours_2 = "9"
        if minutes_1=="?":
            minutes_1="5"
        if minutes_2=="?":
            minutes_2="9"
        s = f"{hours_1}{hours_2}:{minutes_1}{minutes_2}"
        return s 
   
answer = Solution().findLatestTime("1?:?4") 
print(answer)
answer = Solution().findLatestTime("?3:12") 
answer = Solution().findLatestTime("?3:12") 

print(answer)
print(answer)
answer = Solution().findLatestTime("?1:?6") 
answer = Solution().findLatestTime("?1:?6") 
answer = Solution().findLatestTime("?1:?6") 