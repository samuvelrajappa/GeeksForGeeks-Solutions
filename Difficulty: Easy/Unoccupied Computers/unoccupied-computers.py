class Solution:
    def solve(self, n, s):
        # code here
        using_computer = set()
        rejected = set()
        rejected_count = 0
        
        for customer in s:
            # First occurrence: Customer Arrives
            if customer not in using_computer and customer not in rejected:
                if len(using_computer) < n:
                    using_computer.add(customer)
                else:
                    rejected.add(customer)
                    rejected_count += 1
            
            # Second occurrence: Customer Departs
            else:
                if customer in using_computer:
                    using_computer.remove(customer)
                elif customer in rejected:
                    rejected.remove(customer)
                    
        return rejected_count