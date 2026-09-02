class Solution:
    def isPossible(self, arr, s, x):
        # code here 
        if x == 0:
            return True

        # P stores the sequence of numbers on the paper
        P = [s]
        current_sum = s

        # Generate the sequence up to the point where elements exceed x
        for num in arr:
            if P[-1] > x:
                break
            next_p = current_sum + num
            P.append(next_p)
            current_sum += next_p

        # Greedily pick elements from largest to smallest
        for val in reversed(P):
            if x >= val:
                x -= val

        return x == 0