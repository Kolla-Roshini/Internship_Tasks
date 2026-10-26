# Introduction to Sets
# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem




def average(array):
    arr=set(array)

    sum=0
    total=len(arr)
    for x in arr:
        sum = sum+x
    avg=sum/total
    return avg
    
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)