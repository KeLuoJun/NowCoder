import math
from bisect import *
mod = 10 ** 9 + 7
n = int(input().strip())
a, s, p, fac = list(map(int, input().split())), 0, [0] * (n + 1), [1] * (n + 1)
a.sort()

for i in range(1, n + 1):
    fac[i] = fac[i - 1] * i % mod
for i, v in enumerate(a):
    p[i + 1] = (p[i] + v) % mod
    t1 = (v * i - p[i]) % mod
    s += (fac[n - 1] * t1 * 2) % mod

ans = s * pow(fac[n], -1, mod) % mod
print(ans)