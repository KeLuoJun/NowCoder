n = int(input())
s = input().strip()

pre0_p = [0] * (n + 1)
pre1_p = [0] * (n + 1)

current_pre0 = 0
current_pre1 = 0

pre0_p[0] = current_pre0
pre1_p[0] = current_pre1

for i in range(1, n + 1):
    c = s[i-1]
    if c == '0':
        current_pre0 ^= 1
    else:
        current_pre1 ^= 1
    pre0_p[i] = current_pre0
    pre1_p[i] = current_pre1

# 初始化状态最后出现位置数组
state_last = [[-1 for _ in range(2)] for _ in range(2)]

for j in range(n + 1):
    a = pre0_p[j]
    b = pre1_p[j]
    if j > state_last[a][b]:
        state_last[a][b] = j

count = 0
for k in range(1, n + 1):
    if k == n:
        continue  # 删除所有字符，无法形成非空字符串
    a = pre0_p[k]
    b = pre1_p[k]
    j_max = state_last[a][b]
    if j_max >= k + 1:
        count += 1

probability = count / n
print("{0:.6f}".format(probability))