class Solution:
    def searchWord(self, mat, word):
        # code here
        n = len(mat)
        m = len(mat[0])
        w_len = len(word)
        res = []
        
        # Define the 8 directions: Up, Down, Left, Right, and 4 Diagonals
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),   # Vertical & Horizontal
            (-1, -1), (-1, 1), (1, -1), (1, 1)  # Diagonals
        ]
        
        # Traverse every cell in the grid
        for r in range(n):
            for c in range(m):
                # If the first character matches, check all 8 directions
                if mat[r][c] == word[0]:
                    found = False
                    
                    for dr, dc in directions:
                        curr_r, curr_c = r, c
                        k = 1
                        
                        # Match the remaining characters in a straight line
                        while k < w_len:
                            curr_r += dr
                            curr_c += dc
                            
                            # Boundary check and character match check
                            if not (0 <= curr_r < n and 0 <= curr_c < m) or mat[curr_r][curr_c] != word[k]:
                                break
                            k += 1
                        
                        # If the entire word is successfully matched
                        if k == w_len:
                            found = True
                            break
                    
                    # If found in any of the 8 directions, add the starting coordinate
                    if found:
                        res.append([r, c])
                        
        return res