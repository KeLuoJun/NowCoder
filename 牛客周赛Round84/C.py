import sys


def main() -> None:
    data = sys.stdin.read().split()
    idx = 0
    n, k = map(int, data[idx:idx + 2])
    idx += 2
    s = data[idx:]
    s = ''.join(s)
    ans = 0
    for i in range(len(s) - k + 1):
        for j in range(i + 1, i + k):
            ans += abs(ord(s[j]) - ord(s[j - 1]))
    print(ans)

if __name__ == '__main__':
    main()
