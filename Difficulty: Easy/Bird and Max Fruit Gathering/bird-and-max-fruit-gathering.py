class Solution:

    def maxFruits(self, arr: list[int], m: int) -> int:
        """ code here """
        n = len(arr)
        
        # If the bird can visit all trees, return the total sum
        if m >= n:
            return sum(arr)
        
        # Calculate the sum of the first window of size m
        curr_sum = sum(arr[:m])
        max_sum = curr_sum
        
        # Slide the window across the circular array
        for i in range(1, n):
            # Remove the element leaving the window (i - 1)
            # Add the element entering the window ((i + m - 1) % n)
            curr_sum = curr_sum - arr[i - 1] + arr[(i + m - 1) % n]
            
            if curr_sum > max_sum:
                max_sum = curr_sum
                
        return max_sum