import sys
def main() -> None:
    x, y, z = map(int, sys.stdin.readline().strip().split())
    ans = min(x * y, z)
    print(ans)


if __name__ == '__main__':
    main()

