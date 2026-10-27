# Caesar Cipher
# https://www.hackerrank.com/challenges/caesar-cipher-1/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    new_string = ""
    for char in s:
        if char.isalpha():
            min_limit = ord("a") if char.islower() else ord("A")
            max_limit = ord("z") if char.islower() else ord("Z")
            pos = ord(char) + (k % 26)

            if min_limit <= pos <= max_limit:
                new_string += chr(pos)
            elif pos > max_limit:
                new_string += chr((pos - max_limit) + (min_limit - 1))
        else:
            new_string += char

    return new_string
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()