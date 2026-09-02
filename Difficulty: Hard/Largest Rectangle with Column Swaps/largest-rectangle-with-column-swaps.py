class Solution:
    def maxArea(self, mat: list[list[int]]) -> int:
        # code here
        if not mat or not mat[0]:
            return 0
        
        n = len(mat)
        m = len(mat[0])
        
        # heights[j] stores consecutive 1s extending upward in column j
        heights = [0] * m
        max_area = 0
        
        for i in range(n):
            for j in range(m):
                # If current cell is 1, increment height; otherwise, reset to 0
                if mat[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            # Sort heights in descending order to simulate optimal column swapping
            sorted_heights = sorted(heights, reverse=True)
            
            # Compute the maximum rectangle area for the current row configuration
            for k in range(m):
                area = sorted_heights[k] * (k + 1)
                if area > max_area:
                    max_area = area
                    
        return max_area