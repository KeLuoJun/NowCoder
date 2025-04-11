import sys


def main():
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    h = [0] * n
    for i in range(n):
        if i == 0:
            h[i] = a[i] - 1 + 2
        else:
            h[i] = a[i] - 1
        h[i] = 5 if h[i] > 5 else h[i]
    h = [str(x) for x in h]
    print(" ".join(h))

if __name__ == '__main__':
    main()