import sys
# Increase recursion depth for safety
sys.setrecursionlimit(2000)


class Solution:
    def minCount(self, arr):
        """ code here """
        n = len(arr)
        
        # Memoization table to store results of subproblems
        # State: (index, last_increasing_value, last_decreasing_value)
        memo = {}
        
        def solve(i, last_inc, last_dec):
            # Base case: if we processed all elements
            if i == n:
                return 0
                
            state = (i, last_inc, last_dec)
            if state in memo:
                return memo[state]
            
            # Option 1: Skip the current element
            max_elements = solve(i + 1, last_inc, last_dec)
            
            # Option 2: Add to the increasing subsequence
            if arr[i] > last_inc:
                max_elements = max(max_elements, 1 + solve(i + 1, arr[i], last_dec))
                
            # Option 3: Add to the decreasing subsequence
            if arr[i] < last_dec:
                max_elements = max(max_elements, 1 + solve(i + 1, last_inc, arr[i]))
                
            memo[state] = max_elements
            return max_elements

        # Initial values: 
        # last_inc = 0 (smaller than any possible element >= 1)
        # last_dec = 101 (larger than any possible element <= 100)
        max_included = solve(0, 0, 101)
        
        return n - max_included