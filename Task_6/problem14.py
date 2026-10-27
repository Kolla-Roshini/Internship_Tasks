# Problem: Set .intersection() Operation
# Link: https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

e, a = int(input()), set(map(int, input().split()))
f, b = int(input()), set(map(int, input().split()))

print(len(a & b))