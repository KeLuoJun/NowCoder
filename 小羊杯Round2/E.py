
def main() -> None:
    T = int(input())
    ans = []
    for _ in range(T):
        count = 0
        a, b, c = map(int, input().split())
        for x in [a, b, c]:
            for y in [a, b, c]:
                if x > y:
                    continue
                for z in [a, b, c]:
                    if z >= y and x + y > z:
                        count += 1
        ans.append(count)
    return ans



if __name__ == '__main__':
    ans = main()
    for a in ans:
        print(a)
