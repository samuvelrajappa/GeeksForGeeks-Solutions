class Solution:
    def pairAndSum(self, arr):
        # code here
        total_sum = 0
        
        # Loop through each bit position up to 32 bits
        for k in range(32):
            count = 0
            # Count elements that have the k-th bit set
            for num in arr:
                if (num & (1 << k)) != 0:
                    count += 1
            
            # Number of valid pairs for this bit position
            pairs = (count * (count - 1)) // 2
            
            # Add the contribution of this bit position to the total sum
            total_sum += pairs * (1 << k)
            
        return total_sum