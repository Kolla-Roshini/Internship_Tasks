# Problem: Set .union() Operation
# Link: https://www.hackerrank.com/challenges/py-set-union/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
arr=set(map(int,input().split()))
m=int(input())
arr2=set(map(int,input().split()))
l=set()
for i in arr:
    l.add(i)
    for j in arr2:
        l.add(j)
print(len(l))