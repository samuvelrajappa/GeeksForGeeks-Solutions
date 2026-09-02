class Solution:
    def countSubsequences(self, s, n):
        # code here
        MOD = 10**9 + 7
        
        # dp[rem] stores the count of non-empty subsequences with remainder 'rem'
        dp = [0] * n
        
        for char in s:
            digit = int(char)
            # Copy the current DP state to track changes for this digit
            next_dp = list(dp)
            
            # Choice 1: Start a new single-digit subsequence
            next_dp[digit % n] = (next_dp[digit % n] + 1) % MOD
            
            # Choice 2: Append the current digit to all existing subsequences
            for rem in range(n):
                if dp[rem] > 0:
                    new_rem = (rem * 10 + digit) % n
                    next_dp[new_rem] = (next_dp[new_rem] + dp[rem]) % MOD
            
            # Move to the next state
            dp = next_dp
            
        return dp[0]