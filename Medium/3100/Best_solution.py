class Solution:
    def maxBottlesDrunk(self, B: int, E: int) -> int:
        ans, res, e = B, B, E
        while res >= e:
            ans += 1
            res -= e - 1
            e += 1
        return ans
        