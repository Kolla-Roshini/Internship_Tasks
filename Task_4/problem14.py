# Set .add()
# https://www.hackerrank.com/challenges/py-set-add/problem
total_number = int(input())
country = set()
for _ in range(total_number):
    country.add(input())
print(len(country))
