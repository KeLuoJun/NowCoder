import sys

def main() -> None:
    n, k = map(int, sys.stdin.readline().split())
    if n == 0:
        print(0)
        return
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    if k == 0:
        print(n)
        return
    if k == n:
        print(0)
        return
    
    def solve(x):
        if x == 0:
            return n
        m = 0
        contributions = [0] * (n + 1)
        stack = [(1, None, False)]  # 后序遍历的栈
        while stack:
            node, parent, is_visited = stack.pop()
            if not is_visited:
                stack.append((node, parent, True))
                for v in adj[node]:
                    if v != parent:
                        stack.append((v, node, False))
            else:
                sum_childern = 0
                for v in adj[node]:
                    if v != parent:
                        sum_childern += contributions[v]
                total = sum_childern + 1
                if total > x:
                    m += 1
                    contributions[node] = 0
                else:
                    contributions[node] = total
        return m
    
    l, r = 1, n
    ans = n
    while l <= r:
        mid = (l + r) // 2
        if solve(mid) <= k:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    print(ans)



if __name__ == '__main__':
    main()
