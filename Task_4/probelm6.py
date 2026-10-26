#  Find the Runner-Up Score!
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    a=list(set(arr))
    if len(a)<2:
        pass
    else:
        a.sort()
        print(a[-2])
