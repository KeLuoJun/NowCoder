import sys


def main() -> None:
    data = list(map(int, sys.stdin.read().strip().split()))
    ptr = 0
    d, p, q = data[ptr], data[ptr + 1], data[ptr + 2]
    ptr += 3
    for _ in range(q):
        l, r = data[ptr], data[ptr + 1]
        ptr += 2
        cur = 1
        cur = (cur + d) % p
        cycle = 2
        while cur != 1:
            cur = (cur + d) % p
            cycle += 1
        cycle -= 1
        ans = min((r - l + 1), cycle)
        print(ans)


if __name__ == '__main__':
    main()
