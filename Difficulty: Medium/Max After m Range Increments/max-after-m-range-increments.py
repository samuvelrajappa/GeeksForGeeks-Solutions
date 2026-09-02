class Solution:
    def findMax(self, n, a, b, k):
        # code here
        diff = [0] * (n + 1)

        # Apply the range update operations
        for i in range(len(a)):
            diff[a[i]] += k[i]
            if b[i] + 1 < n:
                diff[b[i] + 1] -= k[i]

        # Reconstruct the final values using prefix sums
        max_val = 0
        current_sum = 0
        for i in range(n):
            current_sum += diff[i]
            if current_sum > max_val:
                max_val = current_sum

        return max_val