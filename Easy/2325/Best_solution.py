class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key = [char for char in key if char != " "]
        newKey = ""
        for char in key:
            if char not in newKey:
                newKey += char
        dic = {" ": " "}
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        res = ""
        for keyChar, char in zip(newKey, alphabet):
            dic[keyChar] = char
        for char in message:
            res += dic[char]
        return res
answer = Solution().decodeMessage(key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv")
print(answer)