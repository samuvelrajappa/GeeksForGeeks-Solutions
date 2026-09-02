class Solution:
    def prefixStrings(self, n: int) -> int:
        # code here
        MOD = 10**9 + 7
        
        # dp[i] stores the i-th Catalan number
        dp = [0] * (n + 1)
        dp[0] = 1
        if n >= 1:
            dp[1] = 1
            
        # Compute Catalan numbers using Dynamic Programming
        for i in range(2, n + 1):
            res = 0
            for j in range(i):
                res = (res + dp[j] * dp[i - 1 - j]) % MOD
            dp[i] = res
            
        return dp[n]