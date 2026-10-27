# Problem: Symmetric Difference
# Link: https://www.hackerrank.com/challenges/symmetric-difference/problem


# Enter your code here. Read input from STDIN. Print output to STDOUT

m = int(input())
aset = set(map(int, input().split()))
n = int(input())
bset = set(map(int, input().split()))
diff = sorted(aset.difference(bset).union(bset.difference(aset)))
for i in diff:
  print(i)
