class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        answer_list = []
        for count in range(len(s)):
            answer_count = 0
            alphabets = {}
            for word in s[count:]:
                if word not in alphabets.keys():
                    alphabets[word]=1
                    answer_count+=1
                elif alphabets[word]<2:
                    alphabets[word]+=1
                    answer_count+=1
                else:
                    answer_list.append(answer_count)
                    answer_count=1
                    alphabets = {}
                    alphabets[word]=1
            answer_list.append(answer_count)
        return max(answer_list)
    
answer = Solution().maximumLengthSubstring("ccbcb")
print(answer)