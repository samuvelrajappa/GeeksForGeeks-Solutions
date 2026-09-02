class Solution:
    def palindromicStrings(self, n, k):
        # code here
        MOD = 10**9 + 7
        total_strings = 0
        
        # Iterate over all possible string lengths up to n
        for length in range(1, n + 1):
            # Number of distinct characters needed to build the palindrome
            num_distinct = (length + 1) // 2
            
            # Compute the permutation P(k, num_distinct) modulo 10^9 + 7
            ways = 1
            for i in range(num_distinct):
                ways = (ways * (k - i)) % MOD
                
            # Add to total combinations
            total_strings = (total_strings + ways) % MOD
            
        return total_strings