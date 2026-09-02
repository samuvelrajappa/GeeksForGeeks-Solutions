import bisect

class Solution:

    def getMarks(self, l, r, rank):
        """code here"""
        prefix_counts = []
        current_total = 0
        
        for i in range(len(l)):
            interval_size = r[i] - l[i] + 1
            current_total += interval_size
            prefix_counts.append(current_total)
            
        ans = []
        
        # Step 2: Answer each query using binary search
        for q in rank:
            # Find the first interval where prefix_counts[idx] >= q
            idx = bisect.bisect_left(prefix_counts, q)
            
            # Find how many elements lie before this interval
            elements_before = prefix_counts[idx - 1] if idx > 0 else 0
            
            # Find the position/offset within the current interval
            offset = q - elements_before - 1
            
            # Compute the actual mark value
            mark = l[idx] + offset
            ans.append(mark)
            
        return ans