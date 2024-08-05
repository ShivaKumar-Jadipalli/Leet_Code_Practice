class Solution:
    def __init__(self) -> None:
        self.occured = []
        self.status = False 
    def canReach(self, arr, start):
        if start >= len(arr) or start < 0 or start in self.occured:
            return False
        if arr[start] == 0:
            self.status = True
            return True
        self.occured.append(start)
        if self.canReach(arr, start+arr[start]): # just so that we don't continue further even if the case is true 
            return True
        self.canReach(arr , start-arr[start])
        return self.status
print(Solution().canReach( arr = [4,2,3,0,3,1,2], start = 5))
print(Solution().canReach(arr = [4,2,3,0,3,1,2], start = 0))
print(Solution().canReach(arr = [3,0,2,1,2], start = 2))