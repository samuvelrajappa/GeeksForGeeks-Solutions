class Solution:
    def count(self, n: int, m: int) -> int:
        # code here
        neighbors = [[] for _ in range(m + 1)]
        for i in range(1, m + 1):
            unique_neighbors = set()

            # Add all multiples of i up to m
            for mul in range(i, m + 1, i):
                unique_neighbors.add(mul)

            # Add all divisors of i
            for div in range(1, int(i**0.5) + 1):
                if i % div == 0:
                    unique_neighbors.add(div)
                    unique_neighbors.add(i // div)

            neighbors[i] = list(unique_neighbors)

        # Step 2: Initialize DP table for length 1
        # dp[j] stores the number of valid sequences ending with j
        dp = [1] * (m + 1)
        dp[0] = 0 # 0 is not a valid element in the range [1, m]

        # Step 3: Transition for sequences of length 2 up to n
        for _ in range(2, n + 1):
            next_dp = [0] * (m + 1)
            for j in range(1, m + 1):
                if dp[j] > 0:
                    for nbr in neighbors[j]:
                        next_dp[nbr] += dp[j]
            dp = next_dp

        # Step 4: The answer is the sum of all valid sequences of length n
        return sum(dp)