class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        previous = s[0]
        for i in s[1:]:
            if f"{previous}{i}"==f"{i}{previous}":
                return True
            previous=i 
        return False
print(Solution().isSubstringPresent("leetcode"))
print(Solution().isSubstringPresent("abcba"))
print(Solution().isSubstringPresent("abcd"))
