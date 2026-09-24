class Solution:
    def maxStackHeight(self, r: list[int], h: list[int]) -> int:
        # Pair radius and height together
        discs = list(zip(r, h))

        # Sort by radius ascending, and height descending for ties
        discs.sort(key=lambda x: (x[0], -x[1]))

        # Since 1 <= h[i] <= 1000, we use a Fenwick tree of size 1001
        MAX_H = 1001
        bit = [0] * (MAX_H + 1)

        # Function to update the maximum stack height at a specific disc height
        def update(idx, val):
            while idx <= MAX_H:
                if val > bit[idx]:
                    bit[idx] = val
                idx += idx & (-idx)

        # Function to query the maximum stack height possible with a height < idx
        def query(idx):
            res = 0
            while idx > 0:
                if bit[idx] > res:
                    res = bit[idx]
                idx -= idx & (-idx)
            return res

        # Process each disc
        for radius, height in discs:
            # Find the best valid stack height from strictly smaller discs
            max_prev = query(height - 1)
            current_dp = max_prev + height
            # Update the Fenwick tree with the new cumulative height
            update(height, current_dp)

        # The maximum value in the Fenwick tree is our answer
        return query(MAX_H)
