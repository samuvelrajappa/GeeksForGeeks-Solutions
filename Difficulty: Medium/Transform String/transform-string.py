class Solution:
    def transform(self, s1, s2): 
        #code here
        if len(s1) != len(s2):
            return -1
        
        # Check if frequencies of all characters are identical
        count = {}
        for char in s1:
            count[char] = count.get(char, 0) + 1
        for char in s2:
            count[char] = count.get(char, 0) - 1
            
        for val in count.values():
            if val != 0:
                return -1
                
        # Two-pointer matching from the end of both strings
        res = 0
        i = len(s1) - 1
        j = len(s2) - 1
        
        while i >= 0:
            # If characters match, move both pointers backward
            if s1[i] == s2[j]:
                i -= 1
                j -= 1
            # If they don't match, s1[i] needs to be picked and moved to the front
            else:
                res += 1
                i -= 1
                
        return res