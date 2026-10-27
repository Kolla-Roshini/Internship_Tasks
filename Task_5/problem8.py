# Problem: Set .add()
# Link: https://www.hackerrank.com/challenges/py-set-add/problem


# Enter your code here. Read input from STDIN. Print output to STDOUT
total_number = int(input())
country = set()
for _ in range(total_number):
    country.add(input())
print(len(country))
