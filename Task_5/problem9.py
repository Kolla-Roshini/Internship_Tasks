# Problem: Word Order
# Link: https://www.hackerrank.com/challenges/word-order/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
import sys

def solve():
    # Read all lines from standard input
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    n = int(input_data[0])
    words = input_data[1:n+1]
    
    # Counter preserves insertion order in Python 3.7+
    word_counts = Counter(words)
    
    # 1. Print number of distinct words
    print(len(word_counts))
    
    # 2. Print occurrences corresponding to the order of appearance
    print(*(word_counts.values()))

if __name__ == '__main__':
    solve()
