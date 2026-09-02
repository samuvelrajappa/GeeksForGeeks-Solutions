class Solution:
    def minThrows(self, n, lad, sn):
        # code here
        total_cells = n * n
        # Array to store the shortcut destinations for snakes and ladders
        jump = [0] * (total_cells + 1)

        # Record ladder transitions
        for i in range(0, len(lad), 2):
            jump[lad[i]] = lad[i + 1]

        # Record snake transitions
        for i in range(0, len(sn), 2):
            jump[sn[i]] = sn[i + 1]

        # Queue stores tuples of (current_cell, throw_count)
        queue = deque([(1, 0)])
        visited = [False] * (total_cells + 1)
        visited[1] = True

        while queue:
            curr, throws = queue.popleft()

            # Destination reached
            if curr == total_cells:
                return throws

            # Simulate rolling a 6-sided die
            for dice in range(1, 7):
                next_cell = curr + dice

                if next_cell <= total_cells:
                    # Instantly teleport if landing on a snake or ladder
                    if jump[next_cell] != 0:
                        next_cell = jump[next_cell]

                    # Add to queue if the destination is unvisited
                    if not visited[next_cell]:
                        visited[next_cell] = True
                        queue.append((next_cell, throws + 1))

        return -1