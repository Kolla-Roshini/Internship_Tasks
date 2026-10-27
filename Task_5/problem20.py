# Problem: Piling Up!
# Link: https://www.hackerrank.com/challenges/piling-up/problem


# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

def solve():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        blocks = deque(map(int, input().split()))
        
        last_block = float('inf')
        possible = True
        
        while blocks:
           
            if blocks[0] >= blocks[-1]:
                candidate = blocks.popleft()
            else:
                candidate = blocks.pop()
                
           
            if candidate > last_block:
                possible = False
                break
                
            last_block = candidate
            
        print("Yes" if possible else "No")

if __name__ == '__main__':
    solve()