# Problem: Validating the Phone Number
# Link: https://www.hackerrank.com/challenges/validating-the-phone-number/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())

for i in range(N):

    mobile = input().strip()

    if len(mobile) == 10 and mobile.isdigit() and mobile[0] in ['7','8','9']:
        print("YES")
    else:
        print("NO")