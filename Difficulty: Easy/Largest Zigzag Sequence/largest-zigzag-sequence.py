class Solution:
    def zigzagSequence(self, mat):
        # code here
        n = len(mat)
        if n == 1:
            return mat[0][0]

        # dp[j] stores the maximum zigzag sequence sum ending at column j
        dp = mat[0][:]

        for i in range(1, n):
            # Find the top two maximum values and their indices from the previous row
            max1_val, max1_idx = -1, -1
            max2_val, max2_idx = -1, -1

            for j in range(n):
                if dp[j] > max1_val:
                    max2_val, max2_idx = max1_val, max1_idx
                    max1_val, max1_idx = dp[j], j
                elif dp[j] > max2_val:
                    max2_val, max2_idx = dp[j], j

            # Compute the DP array for the current row
            new_dp = [0] * n
            for j in range(n):
                if j != max1_idx:
                    new_dp[j] = mat[i][j] + max1_val
                else:
                    new_dp[j] = mat[i][j] + max2_val
            dp = new_dp

        return max(dp)