# Finding the Percentage
# https://www.hackerrank.com/challenges/finding-the-percentage/problem
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

grades = student_marks[query_name]
ans = sum(grades)/len(grades)
print(f"{ans:.2f}")
