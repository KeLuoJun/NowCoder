import sys
from heapq import *

def main():
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        n, k = map(int, sys.stdin.readline().strip().split())
        arr = list(map(int, sys.stdin.readline().strip().split()))
        heap = [(-num, -idx) for idx, num in enumerate(arr[1:])]
        heapify(heap)
        for _ in range(k):
            top, idx = heappop(heap)
            arr[0] -= top
            arr[-idx + 1] = None
            
        result = []
        for num in arr:
            if num is not None:
                result.append(num)
        print(" ".join(map(str, result)))
        
if __name__ == '__main__':
    main()