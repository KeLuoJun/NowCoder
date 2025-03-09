import sys

def main() -> None:
    data = sys.stdin.read().split()
    idx = 0
    n, k = map(int, data[idx:idx + 2])
    idx += 2
    s = data[idx]
    s = s.strip()
    temp = [0]
    ans = 0
    for i in range(1, n):
        t = abs(ord(s[i]) - ord(s[i - 1])) + temp[i - 1]
        temp.append(t)
    for i in range(1, n - k + 2):
        ans += temp[i + k - 2] - temp[i - 1]
    print(ans)


if __name__ == '__main__':
    main()
