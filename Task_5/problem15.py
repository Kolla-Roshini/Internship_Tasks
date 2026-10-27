# Problem: Lists
# Link: https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    res = []
for i in range(N):
    temp = input().split()
    if temp[0] == 'insert':
        res.insert(int(temp[1]), int(temp[2]))
    elif temp[0] == 'print':
        print(res) 
    elif temp[0] == 'remove':
        res.remove(int(temp[1]))
    elif temp[0] == 'append':
        res.append(int(temp[1]))
    elif temp[0] == 'sort':
        res.sort()
    elif temp[0] == 'pop':
        res.pop()
    elif temp[0] == 'reverse':
        res.reverse()

