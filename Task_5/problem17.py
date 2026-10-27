# Problem: No Idea!
# Link: https://www.hackerrank.com/challenges/no-idea/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

happiness = 0

# Ignore the first line, it is redundant.
input()

c = Counter([int(i) for i in input().split()])
set_a = [int(i) for i in input().split()]
set_b = [int(i) for i in input().split()]


for n in set_a:
    if n in c:
        happiness += c[n]

for n in set_b:
    if n in c:
        happiness -= c[n]

print(happiness)
