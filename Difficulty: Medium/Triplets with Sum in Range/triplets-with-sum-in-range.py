class Solution:
   
    def countTriplets(self, arr: list[int], l: int, r: int) -> int:
        # code here
        def countLessThanOrEqual(target):
            count = 0
            n = len(arr)
            
            # Iterate through each element as the first element of the triplet
            for i in range(n - 2):
                left = i + 1
                right = n - 1
                
                # Use two pointers for the remaining two elements
                while left < right:
                    current_sum = arr[i] + arr[left] + arr[right]
                    
                    if current_sum <= target:
                        # If the sum is <= target, all elements between left and right 
                        # can form a valid triplet with arr[i] and arr[left]
                        count += (right - left)
                        left += 1
                    else:
                        # Decrease the sum by moving the right pointer inward
                        right -= 1
            return count

        # Sort the array first to enable the two-pointer technique
        arr.sort()
        
        # Result is the triplets in range [0, r] minus triplets in range [0, l-1]
        return countLessThanOrEqual(r) - countLessThanOrEqual(l - 1)