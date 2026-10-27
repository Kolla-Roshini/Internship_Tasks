# Pangrams
# https://www.hackerrank.com/challenges/pangrams/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    i = 0
    length = len(s)
    while len(alphabet) > 0 and i < length:
        alphabet.discard(s[i].lower())
        i+=1
    return "pangram" if len(alphabet) == 0 else "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()