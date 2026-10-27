# Problem: Collections.Counter()
# Link: https://www.hackerrank.com/challenges/collections-counter/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
shoe_num = int(input())
shoe_size = Counter(input().split())
revenue = 0
for _ in range(0,int(input())):
    cus_size, pay = input().split()
    if shoe_size[cus_size] >= 1:
        revenue += int(pay)
        shoe_size[cus_size] -= 1
    else:
        revenue += 0
print(revenue)
