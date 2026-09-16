from typing import List

class Solution:
    def dominantPairs(self, arr: List[int]) -> int:
        n = len(arr)
        m = n // 2
        
        # Step 1: Split and sort both halves independently
        left = sorted(arr[:m])
        right = sorted(arr[m:])
        
        ans = 0
        j = 0
        
        # Step 2: Use two pointers to count dominant pairs
        for i in range(m):
            while j < m and left[i] >= 5 * right[j]:
                j += 1
            ans += j  # All elements from right[0] to right[j-1] are valid for left[i]
            
        return ans
