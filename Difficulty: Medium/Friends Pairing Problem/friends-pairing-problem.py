class Solution:
    def countFriendsPairings(self, n: int) -> int:
        # code here 
        if n <= 2:
            return n

        # 'a' represents dp[i-2], 'b' represents dp[i-1]
        a = 1
        b = 2

        # Compute ways dynamically up to n
        for i in range(3, n + 1):
            c = b + (i - 1) * a
            a = b
            b = c

        return b