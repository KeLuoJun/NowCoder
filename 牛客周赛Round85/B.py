import sys


def main() -> None:
    data = list(map(int, sys.stdin.read().strip().split()))
    idx = 0
    n = data[idx]
    idx += 1
    a = data[idx:idx + n]
    a.sort()
    x = 0
    p = 1
    for i in a:
        x += i * p
        p = -p
    print(x)


if __name__ == '__main__':
    main()
