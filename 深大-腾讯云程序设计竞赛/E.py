# 树的直径问题（两次BFS）
import sys
from collections import deque

def main() -> None:
    n = int(sys.stdin.readline())
    if n == 1:
        print(0)
        return
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)

    def bfs(start):
        visited = [-1] * (n + 1)
        queue = deque([start])
        visited[start] = 0
        max_dist = 0
        far_node = start
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if visited[v] == -1:
                    visited[v] = visited[u] + 1
                    queue.append(v)
                    if visited[v] > max_dist:
                        max_dist = visited[v]
                        far_node = v
        return far_node, max_dist
    
    u, _ = bfs(1)
    v, diameter = bfs(u)
    print(diameter)

if __name__ == '__main__':
    main()

