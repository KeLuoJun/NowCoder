import sys
sys.setrecursionlimit(1 << 25)  # 将 Python 默认的递归深度限制从 1000 调整为 2^25（约 33,554,432 层）

def main() -> None:
    n = int(sys.stdin.readline())
    adj = [[] for _ in range(n + 1)]
    total = 0
    for _ in range(n - 1):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
        total += abs(u - v)

    stack = []
    root = 1
    stack.append((root, -1, False))
    sub = [0] * (n + 1)
    min_diff = float('inf')

    while stack:
        node, parent, visited = stack.pop()
        if not visited:
            stack.append((node, parent, True))
            for v in adj[node]:
                if v != parent:
                    stack.append((v, node, False))
        else:
            current_sub = 0
            for v in adj[node]:
                if v != parent:
                    current_sub += sub[v] + abs(node - v)
            sub[node] = current_sub
            if parent != -1:
                w = abs(node - parent)
                current_diff = abs(2 * sub[node] - (total - w))
                min_diff = min(min_diff, current_diff)
    print(min_diff)

if __name__ == '__main__':
    main()
