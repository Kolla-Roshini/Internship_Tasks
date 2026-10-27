# Set .symmetric_difference() Operation
# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input()) 
arr = set(map(int,input().split())) 
b = int(input()) 
arr2 = set(map(int,input().split()))

result = arr.symmetric_difference(arr2) 
print(len(result))