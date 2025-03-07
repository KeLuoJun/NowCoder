import sys



def main() -> None:
    n = int(sys.stdin.readline())
    if n == 0:
        print(0)
        return
    s = [sys.stdin.readline().strip() for _ in range(n)]

    if n == 1:
        print(0)
        return
    
    left = [1] * n
    for i in range(1, n):
        if s[i] == s[i - 1]:
            left[i] = left[i - 1] + 1
        
    right = [1] * n
    for i in range(n - 2, -1, -1):
        if s[i] == s[i + 1]:
            right[i] = right[i + 1] + 1
    
    max_original = 0
    for i in range(n):
        if left[i] >= 2 and left[i] > max_original:
            max_original = left[i]
        
    max_merge = 0
    for i in range(1, n - 1):
        if s[i - 1] == s[i + 1]:
            current = left[i - 1] + right[i + 1]
            if current >= 2 and current > max_merge:
                max_merge = current
    ans = max(max_merge, max_original)
    print(ans)

if __name__ == '__main__':
    main()


