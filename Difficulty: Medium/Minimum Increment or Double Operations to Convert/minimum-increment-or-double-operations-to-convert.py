class Solution:
    def countMinOperations(self, arr):
        # code here
        total_increments = 0
        max_doubles = 0

        for num in arr:
            if num == 0:
                continue

            increments = 0
            doubles = 0

            # Reduce the current number to 0 by tracking operations
            while num > 0:
                if num % 2 == 1:
                    increments += 1
                    num -= 1
                else:
                    doubles += 1
                    num //= 2

            total_increments += increments
            max_doubles = max(max_doubles, doubles)

        return total_increments + max_doubles