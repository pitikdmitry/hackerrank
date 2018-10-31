#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the isValid function below.
def isValid(s) -> None:
    counter = Counter()

    for c in s:
        counter[c] += 1

    one_mistake = False
    frequensy = Counter()
    for key, value in counter.items():
        frequensy[value] += 1

    if len(frequensy) == 1:
        print("YES")
        return
    elif len(frequensy) == 2:
        one_flag = False
        items = []
        for value, freq in frequensy.items():
            items.append((value, freq))
            if freq == 1:
                one_flag = True

        if one_flag:
            if abs(items[0][0] - items[1][0]) == 1 or (items[0][0] == 1 and items[0][1] == 1) or (items[1][0] == 1 and items[1][1] == 1):
                print("YES")
                return
            else:
                print("NO")
                return
        else:
            print("NO")
            return

    else:
        print("NO")
        return


s = input()

isValid(s)
