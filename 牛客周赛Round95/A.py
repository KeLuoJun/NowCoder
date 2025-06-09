import sys

def main() -> None:
    l, r = map(int, sys.stdin.readline().split())
    if l != r:
        print(2)
    else:
        print(1)

if __name__ == '__main__':
    main()
