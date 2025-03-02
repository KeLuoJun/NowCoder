import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    ptr = 0
    T = int(data[ptr])
    ptr += 1
    for _ in range(T):
        n = int(data[ptr])
        ptr += 1
        adj = [[] for _ in range(n + 1)]
        degrees = [0] * (n + 1)
        for __ in range(n - 1):
            u = int(data[ptr])
            v = int(data[ptr + 1])
            ptr += 2
            adj[u].append(v)
            adj[v].append(u)
            degrees[u] += 1
            degrees[v] += 1
        
        if n == 2:
            print("YES")
            continue
        
        # BFS to find the farthest node from a start node
        def bfs(start):
            visited = [False] * (n + 1)
            q = deque()
            q.append((start, -1, 0))  # (node, parent, distance)
            max_dist = 0
            far_node = start
            while q:
                u, p, d = q.popleft()
                if d > max_dist:
                    max_dist = d
                    far_node = u
                for v in adj[u]:
                    if v != p and not visited[v]:
                        visited[v] = True
                        q.append((v, u, d + 1))
            return far_node
        
        # Find the two ends of the diameter
        u = bfs(1)
        v = bfs(u)
        
        # Reconstruct the path from u to v using BFS
        parent = [0] * (n + 1)
        visited = [False] * (n + 1)
        q = deque([u])
        visited[u] = True
        found = False
        while q and not found:
            node = q.popleft()
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    parent[neighbor] = node
                    q.append(neighbor)
                    if neighbor == v:
                        found = True
                        break
        
        # Build the diameter path
        path = []
        current = v
        while current != u:
            path.append(current)
            current = parent[current]
        path.append(u)
        path_set = set(path)
        
        # Check all non-leaf nodes are in the path
        valid = True
        for node in range(1, n + 1):
            if degrees[node] >= 2 and node not in path_set:
                valid = False
                break
        
        print("YES" if valid else "NO")

if __name__ == "__main__":
    main()