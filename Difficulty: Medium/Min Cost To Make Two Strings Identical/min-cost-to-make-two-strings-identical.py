class Solution:
    def findMinCost(self, s1: str, s2: str, costS1: int, costS2: int) -> int:
        n, m = len(s1), len(s2)

        # Initialize the previous row DP table
        prev = [j * costS2 for j in range(m + 1)]

        # Iteratively update for each character in s1
        for i in range(1, n + 1):
            curr = [0] * (m + 1)
            curr[0] = i * costS1  # Base case for empty s2

            for j in range(1, m + 1):
                if s1[i-1] == s2[j-1]:
                    curr[j] = prev[j-1]
                else:
                    curr[j] = min(prev[j] + costS1, curr[j-1] + costS2)
            prev = curr

        return prev[m]
