import math
from collections import Counter

n = int(input())
arr = list(map(int, input().split()))
min_val = min(arr)
max_val = max(arr)

if min_val == max_val:
    # 所有元素相同的情况
    print(1, 0)
else:
    has_middle = any(x != min_val and x != max_val for x in arr)
    if has_middle:
        count = 2
    else:
        count = 2
    print(count, max_val - min_val)