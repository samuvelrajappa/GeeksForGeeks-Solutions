from collections import deque

class Solution:
    def numberOfCells(self, r: int, c: int, u: int, d: int, mat: list[list[int]]) -> int:
        # code here
        if mat[r][c] == '#':
            return 0
            
        n = len(mat)
        m = len(mat[0])
        
        # Array to store the minimum upward moves spent to reach each cell
        min_u = [[float('inf')] * m for _ in range(n)]
        
        # Queue for 0-1 BFS
        q = deque()
        
        # Initialize the starting cell
        min_u[r][c] = 0
        q.append((r, c))
        
        # Directions for Up, Down, Left, Right
        # (dr, dc, cost_u) -> cost_u is 1 for moving Up, 0 for others
        directions = [(-1, 0, 1), (1, 0, 0), (0, -1, 0), (0, 1, 0)]
        
        ans = 0
        
        while q:
            curr_r, curr_c = q.popleft()
            u_spent = min_u[curr_r][curr_c]
            d_spent = u_spent - r + curr_r
            
            for dr, dc, cost in directions:
                new_r, new_c = curr_r + dr, curr_c + dc
                
                # Check boundaries and obstacles
                if 0 <= new_r < n and 0 <= new_c < m and mat[new_r][new_c] == '.':
                    new_u = u_spent + cost
                    new_d = new_u - r + new_r
                    
                    # Verify if constraints for 'u' and 'd' are satisfied
                    if new_u <= u and new_d <= d:
                        # If a path with fewer upward moves is found
                        if new_u < min_u[new_r][new_c]:
                            min_u[new_r][new_c] = new_u
                            if cost == 0:
                                q.appendleft((new_r, new_c))
                            else:
                                q.append((new_r, new_c))
                                
        # Count all reachable unique cells
        for i in range(n):
            for j in range(m):
                if min_u[i][j] != float('inf'):
                    ans += 1
                    
        return ans