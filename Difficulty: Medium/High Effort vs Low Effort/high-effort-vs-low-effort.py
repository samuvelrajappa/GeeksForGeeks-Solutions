class Solution:
    def maxTask(self, h: list[int], l: list[int]) -> int:
        # code here
        n = len(h)
        if n == 0:
            return 0

        # Base case for the first day (day 0)
        dp_two_back = 0               # Represents dp[i-2]
        dp_one_back = max(h[0], l[0])  # Represents dp[i-1]

        # Iterate through the remaining days
        for i in range(1, n):
            # Option 1: Low-effort today + optimal up to yesterday
            # Option 2: High-effort today + optimal up to 2 days ago (skipping yesterday)
            current = max(dp_one_back + l[i], h[i] + dp_two_back)

            # Move the window forward
            dp_two_back = dp_one_back
            dp_one_back = current

        return dp_one_back