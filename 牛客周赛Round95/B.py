n = int(input().strip())
arr = list(map(int, input().split()))
q = int(input().strip())

for _ in range(q):
    l, r = map(int, input().split())
    start = l - 1  # 转换为 0-based 起始索引
    end = r - 1    # 转换为 0-based 结束索引
    m = end - start + 1  # 输出数组的长度
    
    res = []
    res.append(arr[start])  # 第一个元素 b1 = a_l
    # 计算后续元素：b_i = a_{start+i} - a_{start+i-1} (i >= 2)
    for i in range(1, m):
        idx = start + i
        diff = arr[idx] - arr[idx - 1]
        res.append(diff)
    
    # 输出结果，空格分隔
    print(" ".join(map(str, res)))