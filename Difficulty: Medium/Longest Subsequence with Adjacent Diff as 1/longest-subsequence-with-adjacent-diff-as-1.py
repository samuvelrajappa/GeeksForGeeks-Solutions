class Solution:
    def longestSubseq(self, arr):
        # code here
        dp = {}
        max_length = 0
        
        for num in arr:
            # Check the lengths of subsequences ending in num - 1 and num + 1
            prev_len = dp.get(num - 1, 0)
            next_len = dp.get(num + 1, 0)
            
            # The current number can extend either subsequence
            dp[num] = max(prev_len, next_len) + 1
            
            # Track the global maximum length
            if dp[num] > max_length:
                max_length = dp[num]
                
        return max_length