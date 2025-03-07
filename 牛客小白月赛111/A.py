v = list(map(int, input().split()))
a = list(map(int, input().split()))

def permutations(current, remaining, result):
    if not remaining:
        result.append(current.copy())
    for i in range(len(remaining)):
        current.append(remaining[i])
        permutations(current, remaining[:i] + remaining[i+1:], result)
        current.pop()

res = []
permutations([], a, res)

        
found = False
for perm in res:
    wins = 0
    if perm[0] > v[0]:
        wins += 1
    if perm[1] > v[1]:
        wins += 1
    if perm[2] > v[2]:
        wins += 1
    if wins >= 2:
        found = True
        break

print("Yes" if found else "No")