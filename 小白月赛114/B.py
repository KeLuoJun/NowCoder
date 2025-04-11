import sys

def main():
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    a.sort()
    ans = 0
    for i in range(n):
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if a[mid] == (i + 1):
                ans += (i + 1)
                break
            elif a[mid] < (i + 1):
                l = mid + 1
            else:
                r = mid - 1
    print(ans)

if __name__ == '__main__':
    main()