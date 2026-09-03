class Solution:
    def maxDiffSum(self, arr):
        # code here
        if not arr:
            return 0
            
        # Base case for the first element
        keep = 0
        replace = 0
        
        for i in range(1, len(arr)):
            # Calculate next states based on previous keep and replace values
            next_keep = max(keep + abs(arr[i] - arr[i-1]), replace + abs(arr[i] - 1))
            next_replace = max(keep + abs(1 - arr[i-1]), replace + 0) # abs(1 - 1) is 0
            
            # Update states for the next iteration
            keep = next_keep
            replace = next_replace
            
        return max(keep, replace)