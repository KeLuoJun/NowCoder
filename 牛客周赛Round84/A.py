import sys

def main() -> None:
    data = sys.stdin.read().split()
    a = [0] * 3
    for idx in range(3):
        a[idx] = int(data[idx])
        if idx > 0:
            if abs(a[idx] - a[idx - 1]) != 0:
                print('No')
                return
    print("Yes")
    return
    
    


if __name__ == '__main__':
    main()
