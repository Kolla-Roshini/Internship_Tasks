# Super Reduced String
# https://www.hackerrank.com/challenges/reduced-string/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    while re.search(r'([a-z])\1', s):
        s = re.sub(r'([a-z])\1', '', s)
    return 'Empty String' if len(s) == 0 else s
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()