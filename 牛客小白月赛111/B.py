n = int(input())
s = input()

ans = 0
nnum = 0
for c in s:
    if c == 'y':
        ans += 1
        nnum = 0
    else:
        nnum += 1
    if nnum % 2 == 0 and nnum > 0:
        ans += 1
        nnum = 0

print(ans)
