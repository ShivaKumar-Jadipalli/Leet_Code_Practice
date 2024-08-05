class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        right = 0
        cnt = {}
        res = 0
        while right < len(s):
            while right < len(s) and (s[right] not in cnt or cnt[s[right]] < 2):
                cnt[s[right]] = cnt.get(s[right], 0) + 1
                right += 1
            if right == len(s):
                return max(res, right-left)
            res = max(res, right-left)
            # print('r', left, right)
            while s[left] != s[right]:
                cnt[s[left]] -= 1
                left += 1
            cnt[s[left]] -= 1
            left += 1
            res = max(res, right-left)
            # print('l', left, right)
            
            