def solve():
    # Read input
    n, x = map(int, input().split())
    a = [0] + list(map(int, input().split()))  # 1-based indexing
    
    # Array to store the step at which each node is visited
    idx = [-1] * (n + 1)  # -1 means unvisited
    current = x
    step = 0
    
    # Traverse the graph starting from x
    while True:
        if idx[current] != -1:  # Reached a visited node
            if current == x:
                print("Yes")  # x is in a cycle
            else:
                print("No")   # Reached a cycle, but x is not in it
            return
        idx[current] = step
        current = a[current]
        step += 1

# Run the solution
solve()