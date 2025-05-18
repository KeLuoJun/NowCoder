import sys

def solve(n, x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return True
    
    if y2 < y1:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    
    if y1 + 1 == y2:
        if x2 + 1 == x1:
            return True
        elif x1 + 1 == x2 and y2 != n and y2 != n - 1:
            return True
    return False


def main():
    n = int(sys.stdin.readline().strip())
    x1, y1 = map(int, sys.stdin.readline().strip().split())
    x2, y2 = map(int, sys.stdin.readline().strip().split())
    if solve(n, x1, y1, x2, y2):
        print("YES")
    else:
        print("NO")
    
if __name__ == '__main__':
    main()