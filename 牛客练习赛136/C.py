# 算法思路：
# 分割段落 ：通过遍历字符串，将连续相同的字符分割为段，并记录每个段的代价列表。
# 排序代价 ：每个段的代价列表按升序排序，以便后续选择最小代价的复制操作。
# 构建结果字符串 ：
#   对每个段，若当前段字符小于下一段字符，则尝试用最小代价的复制操作，尽可能多地增加该段字符的数量。
#   最终将所有段处理后的结果拼接，形成最终字符串。
# 此方法通过贪心策略选择代价最小的复制操作，确保在左侧尽可能多地复制较小的字符，从而实现字典序最小化。

import sys

def solve(n: int, m: int, s: str, a: list[int]) -> int:
    segments = []
    i = 1
    while i <= n:
        current_char = s[i]
        a_list = []
        j = i 
        while j <= n and s[j] == current_char:
            a_list.append(a[j])
            j += 1
        a_list.sort()
        segments.append([current_char] + a_list)
        i = j
    
    ans = []
    for seg_idx in range(len(segments) - 1):
        current_seg = segments[seg_idx]
        next_seg = segments[seg_idx + 1]
        # 初始添加该段原始长度的字符
        ans.append(current_seg[0] * len(current_seg[1:]))  # seg[0]是字符，后面是a值

        if current_seg[0] < next_seg[0]:
            # 尝试复制该段中的位置，用最小代价的先尝试
            for cost in current_seg[1:]:   # seg[1:]是排序后的a值
                if m >= cost:
                    ans.append(current_seg[0])
                    m -= cost
                else:
                    break
    # 处理最后一个段
    last_seg = segments[-1]
    ans.append(last_seg[0] * len(last_seg[1:]))
    return ''.join(ans)


def main() -> None:
    n, m = map(int, sys.stdin.readline().split())
    s = " " + sys.stdin.readline().strip()
    a = [0] + list(map(int, sys.stdin.readline().split()))
    result = solve(n, m, s, a)
    print(result)


if __name__ == '__main__':
    main()
