def combination(n, k):
    if k < 0 or k > n:
        return 0
    numerator = 1
    denominator = 1
    for i in range(1, k + 1):
        numerator *= (n - i + 1)
        denominator *= i
    return numerator // denominator

def solve(p, x, y):
    ans = 0
    for i in range(x, x+y):
        ans += combination(i, x) * (p**x) * ((1 - p)**(i - x))
    return ans

def main() -> None:
    n, p, q, val = map(int, input().split())
    P = p / q
    result = []
    for _ in range(n):
        x, y = map(int, input().split())
        result.append(round(solve(P, x, y) * ((q**(x + y)) % val)))
    for r in result:
        print(r)


if __name__ == '__main__':
    main()
