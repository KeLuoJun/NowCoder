import sys


def main():
    a, b = map(int, sys.stdin.readline().strip().split())
    if a > b:
        print("Alice")
    else:
        print("Bob")
        
if __name__ == '__main__':
    main()