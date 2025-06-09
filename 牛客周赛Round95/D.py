import sys
from math import gcd
input = sys.stdin.readline

def lowbit(x):
    return x & -x

def query(x):
    res = 0
    while x:
        res += s[x]
        x -= lowbit(x)
    return res

def update(x, a):
    while x <= n:
        s[x] += a
        x += lowbit(x)

q = int(input())

cur = 1
maxx = 0
n = int(3e5 + 5)
s = [0] * (int(3e5 + 5))

for i in range(q):
    l, r = map(int, input().split())
    t = query(r) - query(l - 1)
    if t == 0:
       num = r - l + 1
       if num > maxx:
           cur += num - maxx
           maxx = num
       update(l, 1)
       update(r, 1)
    print(cur)
