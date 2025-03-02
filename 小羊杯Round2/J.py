import math
def main() -> None:
    t = int(input())
    ans = []
    for _ in range(t):
        x, y = map(int, input().split())
        flag = True
        for i in range(2, max(x, y) + 1):
            if math.gcd(x, i) == 1 and math.gcd(y, i) == 1:
                ans.append(i)
                flag = False 
                break
        if flag:
            ans.append(-1)
    for a in ans:
        print(a)


if __name__ == '__main__':
    main()
