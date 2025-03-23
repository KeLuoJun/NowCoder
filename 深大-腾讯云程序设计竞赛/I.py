import sys

def main() -> None:
    n = int(sys.stdin.readline())
    events = []
    for _ in range(n):
        time_str, s = sys.stdin.readline().strip().split(' ', 1)
        h, m = map(int, time_str.split(':'))
        total = h * 60 + m
        events.append((total, s))
    
    events.sort()

    for event in events:
        total, s = event
        h = total // 60
        m = total % 60
        print(f"{h:02d}:{m:02d} {s}")


if __name__ == '__main__':
    main()
