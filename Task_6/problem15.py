# Problem: Set .difference() Operation
# Link: https://www.hackerrank.com/challenges/py-set-difference-operation/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
n= int(input()) 

english = set(map(int, input().split()))

m=int(input()) 
french = set(map(int, input().split()))

op = english - french 
print(len(op))