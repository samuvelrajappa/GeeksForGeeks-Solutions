class Solution:
    def findWays(self, grid):
        # code here
        n = len(grid)
        MOD = 10**9 + 7

        # dp_paths[i][j] stores the number of valid paths to reach (i, j)
        dp_paths = [[0] * n for _ in range(n)]
        # dp_adv[i][j] stores the maximum adventure to reach (i, j)
        dp_adv = [[0] * n for _ in range(n)]

        # Base case initialization
        dp_paths[0][0] = 1
        dp_adv[0][0] = grid[0][0]

        for i in range(n):
            for j in range(n):
                # If the current cell is unreachable, skip it
                if dp_paths[i][j] == 0:
                    continue

                cell_val = grid[i][j]

                # Rule 1 & 3: Move Right (if allowed and within bounds)
                if (cell_val == 1 or cell_val == 3) and j + 1 < n:
                    dp_paths[i][j+1] = (dp_paths[i][j+1] + dp_paths[i][j]) % MOD
                    dp_adv[i][j+1] = max(dp_adv[i][j+1], dp_adv[i][j] + grid[i][j+1])

                # Rule 2 & 3: Move Down (if allowed and within bounds)
                if (cell_val == 2 or cell_val == 3) and i + 1 < n:
                    dp_paths[i+1][j] = (dp_paths[i+1][j] + dp_paths[i][j]) % MOD
                    dp_adv[i+1][j] = max(dp_adv[i+1][j], dp_adv[i][j] + grid[i+1][j])

        # If the destination is unreachable, return [0, 0]
        if dp_paths[n-1][n-1] == 0:
            return [0, 0]

        return [dp_paths[n-1][n-1], dp_adv[n-1][n-1]]