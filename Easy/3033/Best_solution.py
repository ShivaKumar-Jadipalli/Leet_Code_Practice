class Solution:
    def modifiedMatrix(self, a: List[List[int]]) -> List[List[int]]:
        rows = len(a)
        cols = len(a[0])

        for col in range(cols):
            mx = -1
            c = []
            mx = max([row[col] for row in a])
            for row in range(rows):
                if a[row][col] == -1:
                    a[row][col] = mx
        
        return a