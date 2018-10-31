#!/bin/python3

import math
import os
import random
import re
import sys

from math import factorial


def c_n_k(n: int):
    k = 2
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


def sherlockAndAnagrams(s):
    anagrams = {}
    length = 1

    while length < len(s):
        i = 0
        while i < len(s):
            if i + length - 1 < len(s):
                word = s[i:i + length]
                word = ''.join(sorted(word))
                if word not in anagrams:
                    anagrams[word] = 1
                else:
                    anagrams[word] += 1
            i += 1
        length += 1

    result = 0
    for key, value in anagrams.items():
        if value != 1:
            result += c_n_k(value)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

