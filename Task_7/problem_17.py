# Separate the Numbers
# https://www.hackerrank.com/challenges/separate-the-numbers/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    if s[0] == "0":
        print("NO")
        return

    for i in range(1, len(s) // 2 + 1):
        ilk_eded = int(s[:i])
        eded = ilk_eded
        yeni_string = ""

        while len(yeni_string) < len(s):
            yeni_string += str(eded)
            eded += 1

        if yeni_string == s:
            print("YES", ilk_eded)
            return

    print("NO")
    # Write your code here

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)