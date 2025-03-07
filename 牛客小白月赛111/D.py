import sys

def main() -> None:
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1

    a = []
    for _ in range(n):
        row = list(map(int, data[idx:idx + m]))
        a.append(row)
        idx += m
    t = int(data[idx])
    idx += 1

    INF = float('inf')
    v = [[INF] * (m + 1) for _ in range(n + 1)]
    for _ in range(t):
        x = int(data[idx])
        idx += 1
        y = int(data[idx])
        idx += 1
        val = int(data[idx])
        idx += 1
        if val < v[x][y]:
            v[x][y] = val
    
    dp = [[-INF] * (m + 1) for _ in range(n + 1)]
    if v[1][1] > 0:
        dp[1][1] = a[0][0]
    else:
        print(0)
        return
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            k = i + j - 2
            if v[i][j] <= k:
                continue
            max_val = -INF
            if i > 1 and dp[i - 1][j] != -INF:
                max_val = max(max_val, dp[i - 1][j])
            if j > 1 and dp[i][j - 1] != -INF:
                max_val = max(max_val, dp[i][j - 1])
            if max_val != -INF:
                dp[i][j] = max_val + a[i - 1][j - 1]

    max_coins = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            max_coins = max(max_coins, dp[i][j])
    print(max_coins if max_coins != -INF else 0)



if __name__ == '__main__':
    main()

