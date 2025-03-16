import sys

def main() -> None:
    data = list(map(int, sys.stdin.read().strip().split()))
    idx = 0
    n = data[idx]
    idx += 1
    if n % 2 == 0:
        print('yukari')
    else:
        print('kou')

if __name__ == '__main__':
    main()
