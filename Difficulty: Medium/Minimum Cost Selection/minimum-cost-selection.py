class Solution:

    def minCost(self, mat):
        """code here"""
        if not mat:
            return 0
            
        # Initialize costs with the first row values
        prev0, prev1, prev2 = mat[0][0], mat[0][1], mat[0][2]
        
        # Iterate through each row starting from the second one
        for i in range(1, len(mat)):
            # Calculate the current minimum costs for each choice
            curr0 = mat[i][0] + min(prev1, prev2)
            curr1 = mat[i][1] + min(prev0, prev2)
            curr2 = mat[i][2] + min(prev0, prev1)
            
            # Move to the next row
            prev0, prev1, prev2 = curr0, curr1, curr2
            
        # Return the minimum cost possible after reaching the last row
        return min(prev0, prev1, prev2)