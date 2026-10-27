# Problem: Designer Door Mat
# Link: https://www.hackerrank.com/challenges/designer-door-mat/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

N, M = (int(_) for _ in input().split(' '))

p1 = '.|.'
bg = '-'
msg = 'WELCOME'

for i in range(1, N//2+1):
    block = p1*(i*2-1)
    print(block.center(M, bg))
print(msg.center(M, bg))
for i in range(N//2, 0, -1):
    block = p1*(i*2-1)
    print(block.center(M, bg))