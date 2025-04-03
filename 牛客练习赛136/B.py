import sys
import math

def main() -> None:
    n = int(sys.stdin.readline().strip())
    v1, v2 = [], []

    for i in range(1, n + 1):
        if math.gcd(i, 999999999) != 1:
            v1.append(i)
        else:
            v2.append(i)

    t = 2  # 除余后，t=0和t=2从v2取值，t=1从v1取值
    res = []
    while v1 or v2:
        t = (t + 1) % 3
        if t == 0 or t == 2:
            if t == 0 and not v1:
                print("Baka!")
                return
            if v2:
                res.append(v2.pop())
            elif v1:
                res.append(v1.pop())
        elif t == 1:
            if v1:
                res.append(v1.pop())
            else:
                print("Baka!")
                return
    print(" ".join(map(str, res)))
            


if __name__ == '__main__':
    main()
