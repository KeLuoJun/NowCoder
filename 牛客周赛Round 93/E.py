mod = 10 ** 9 + 7
n = int(input())
w = list(map(int, input().split()))

cnt = [0 for _ in range(n + 1)]

for v in w:
    cnt[v] += 1

res = 0
px = 1

def qmi(a, b):
    res = 1
    while b > 0:
        if b & 1:
            res = res * a % mod
        a = a * a % mod
        b >>= 1
    return res
        
for i in range(n + 1):
    v = qmi(2, cnt[i]) - 1
    px *= v
    px %= mod
    if i > 0:
        res += px
        res %= mod
    res += v
    res %= mod
    
print(res)