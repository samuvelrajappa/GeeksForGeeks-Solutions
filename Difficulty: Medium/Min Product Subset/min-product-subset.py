class Solution:
    def minProd(self, arr):
        # code here
        n = len(arr)
        
        # Base case: if there's only one element, it must be selected
        if n == 1:
            return arr[0]
            
        neg_count = 0
        zero_count = 0
        max_neg = float('-inf')
        min_pos = float('inf')
        prod = 1
        
        for x in arr:
            if x == 0:
                zero_count += 1
                continue
            if x < 0:
                neg_count += 1
                max_neg = max(max_neg, x)
            if x > 0:
                min_pos = min(min_pos, x)
                
            prod *= x
            
        # Case 1: No negative numbers found
        if neg_count == 0:
            if zero_count > 0:
                return 0
            return min_pos
            
        # Case 2: Even number of negative numbers
        if neg_count % 2 == 0:
            prod = prod // max_neg
            
        return prod