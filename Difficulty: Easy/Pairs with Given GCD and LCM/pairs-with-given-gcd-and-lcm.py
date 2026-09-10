import math

class Solution:

    def pairCount(self, x, y):
        """code here"""
        # LCM must always be a multiple of GCD
        if y % x != 0:
            return 0
            
        k = y // x
        distinct_prime_factors = 0
        
        # Find the number of distinct prime factors of k
        d = 2
        while d * d <= k:
            if k % d == 0:
                distinct_prime_factors += 1
                while k % d == 0:
                    k //= d
            d += 1
            
        if k > 1:
            distinct_prime_factors += 1
            
        # The number of pairs is 2^p
        return 1 << distinct_prime_factors