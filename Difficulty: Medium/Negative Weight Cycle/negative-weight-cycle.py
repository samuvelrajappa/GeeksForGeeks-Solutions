class Solution:
    def isNegativeWeightCycle(self, V: int, edges: list[list[int]]) -> bool:
        # code here
        dist = [0] * V
        
        # Relax all edges V - 1 times
        for _ in range(V - 1):
            for u, v, w in edges:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    
        # 1st extra iteration to detect any further relaxation
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                return True
                
        return False