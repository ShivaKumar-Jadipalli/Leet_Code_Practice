class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        revs = s[::-1]
        for i in range(1,len(s)):
            if s[i-1:i+1] in revs:
                return True
        return False

# same as ours no diff 