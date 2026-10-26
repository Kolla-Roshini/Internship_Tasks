# Word Order
# https://www.hackerrank.com/challenges/word-order/problem

from collections import OrderedDict

d = OrderedDict()
for _ in range(int(input())):
    string = input()
    d[string] = d.get(string, 0) + 1
print(len(d), ' '.join(map(str,(d.values()))), sep = '\n')
