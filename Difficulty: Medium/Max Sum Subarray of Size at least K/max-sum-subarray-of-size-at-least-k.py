class Solution:
    def maxSumWithK(self, arr: list[int], k: int) -> int:
        # code here
        n = len(arr)

        # Compute the sum of the first k elements
        curr_win_sum = sum(arr[:k])
        max_sum = curr_win_sum

        # Track Kadane's maximum subarray sum for elements before the window
        prev_kadane_sum = 0

        # Slide the window across the array
        for i in range(k, n):
            # Update the sliding window sum of size k
            curr_win_sum += arr[i] - arr[i-k]

            # Compute Kadane's max subarray sum ending at the element that just left the window
            prev_kadane_sum = max(arr[i-k], prev_kadane_sum + arr[i-k])

            # Update max_sum by optionally extending the window with a positive prefix
            max_sum = max(max_sum, curr_win_sum, curr_win_sum + prev_kadane_sum)

        return max_sum