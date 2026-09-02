class Solution:
    def countPairs(self, arr: list[int], k: int) -> int:
        # code here
        arr.sort()

        count = 0
        left = 0
        n = len(arr)

        # Step 2: Use a sliding window with a right pointer
        for right in range(n):
            # Maintain the window where elements have a difference strictly less than k
            while arr[right] - arr[left] >= k:
                left += 1

            # All elements between left and right form a valid pair with arr[right]
            count += (right - left)

        return count