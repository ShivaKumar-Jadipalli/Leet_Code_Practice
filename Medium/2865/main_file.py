class Solution:
    def find_max(self,given,heights):
        results_list = []
        height_len = len(heights)
        for i in given:
            r = heights[i+1] if i+1 < height_len else 0
            m = heights[i]
            l = heights[i-1] if i-1 >= 0 else 0
            results_list.append(r+l+m)
        return given[results_list.index(max(results_list))]
    def merge_split(self,side,given):
        if len(given)==0:
            return []
        if side == "left":
            given = given[::-1]
        previous = given[0]
        answer_list = []
        for i in given:
            if previous >= i:
                answer_list.append(i)
                previous = i
            else:
                answer_list.append(previous)
        return answer_list
    def maximumSumOfHeights(self, heights):
        max_height = max(heights)
        max_positions = [i for i,element in enumerate(heights) if element == max_height]
        if len(max_positions) == 1:
            position = heights.index(max_height) 
        else:
            position = self.find_max(max_positions,heights)
        left_side = self.merge_split("left",heights[:position])
        right_side = self.merge_split("right",heights[position:])
        return sum(left_side + right_side)
answer = Solution().maximumSumOfHeights([1,2,2,2,6,1,4,6,4])
print(answer)