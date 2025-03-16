import sys

def main() -> None:
    data = sys.stdin.read().strip().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    strs = data[idx:idx + t]
    for s in strs:
        sub_0 = 0
        sub_1 = 0
        for i in range(1, len(s)):
            if s[i] == '0' and s[i - 1] == '1':
                sub_1 += 1
            elif s[i] == '1' and s[i - 1] == '0':
                sub_0 += 1
        if s[-1] == '0':
            sub_0 += 1
        if s[-1] == '1':
            sub_1 += 1
        if abs(sub_0 - sub_1) <= 1 and sub_0 + sub_1 <= 5:
            print('Yes')
        else:
            print('No') 
            


if __name__ == '__main__':
    main()
