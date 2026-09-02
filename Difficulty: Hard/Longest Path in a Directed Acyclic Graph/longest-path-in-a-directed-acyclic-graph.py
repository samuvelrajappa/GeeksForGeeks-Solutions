class Solution:
    def maxDistance(self, V, src, edges):
        # code here
        # Step 1: Build the adjacency list
        adj = [[] for _ in range(V)]
        for u, v, w in edges:
            adj[u].append((v, w))

        # Step 2: Perform DFS-based Topological Sort
        visited = [False] * V
        topo_order = []

        def dfs(u):
            visited[u] = True
            for v, w in adj[u]:
                if not visited[v]:
                    dfs(v)
            topo_order.append(u)

        for i in range(V):
            if not visited[i]:
                dfs(i)

        # Reverse to get the correct topological order
        topo_order.reverse()

        # Step 3: Initialize distances with INT_MIN
        INT_MIN = -2147483648
        dist = [INT_MIN] * V
        dist[src] = 0

        # Step 4: Relax edges in topological order
        for u in topo_order:
            if dist[u] != INT_MIN:
                for v, w in adj[u]:
                    if dist[u] + w > dist[v]:
                        dist[v] = dist[u] + w

        return dist