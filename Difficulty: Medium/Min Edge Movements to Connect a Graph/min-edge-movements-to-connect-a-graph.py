class Solution:
    def minEdgesReq(self, n, edges):
        # code here
        if len(edges) < n - 1:
            return -1

        # Step 1: Build the graph adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n
        components = 0

        # Step 2: Traverse components using an iterative DFS
        for i in range(n):
            if not visited[i]:
                components += 1
                visited[i] = True

                # Iterative DFS stack
                stack = [i]
                while stack:
                    curr = stack.pop()
                    for neighbor in adj[curr]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            stack.append(neighbor)

        # Step 3: Minimum movements needed is (components - 1)
        return components - 1