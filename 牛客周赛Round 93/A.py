import sys


def main():
    n = int(sys.stdin.readline().strip())
    if 2**n > n ** 3:
        print("B")
    else:
        print("A")

if __name__ == '__main__':
    main()