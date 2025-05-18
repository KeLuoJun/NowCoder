import sys

def check(s):
    if s[0] == s[2] == s[4] and s[1] == s[3] and s[0] != s[1]:
        return True
    else:
        return False


def main():
    s = sys.stdin.readline().strip()
    n = len(s)
    ans = 0
    for i in range(n-5):
        t = s[i:i + 5]
        if check(t):
            ans += 1
    print(ans)
    
if __name__ == '__main__':
    main()
            
        