class Solution:

    def countWithout(self, n: int, d: int) -> int:
        # code here
        s = str(n)
        m = len(s)

        # dp table to store state: [index][tight][started]
        # index: up to m digits
        # tight: 0 or 1
        # started: 0 or 1
        dp = [[[-1] * 2 for _ in range(2)] for _ in range(m)]

        def solve(idx: int, tight: int, started: int) -> int:
            # Base case: reached the end of the number string
            if idx == m:
                return 1 if started else 0

            # Return cached result if already calculated
            if dp[idx][tight][started] != -1:
                return dp[idx][tight][started]

            # Determine the upper bound for the current digit position
            limit = int(s[idx]) if tight else 9
            ans = 0

            for digit in range(limit + 1):
                new_tight = tight and (digit == limit)
                new_started = started or (digit > 0)

                # If the number has started, check if the digit matches forbidden digit 'd'
                if new_started and digit == d:
                    continue

                ans += solve(idx + 1, new_tight, new_started)

            dp[idx][tight][started] = ans
            return ans

        # Start recursion from index 0, tight=True, started=False
        return solve(0, 1, 0)