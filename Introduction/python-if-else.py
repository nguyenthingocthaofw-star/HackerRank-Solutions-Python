#!/bin/python3

import math
import os
import random
import re
import sys

def check(n):
    if n<1 or n>100:
        return
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0:
        if 2<=n<=5:
            print("Not Weird")
        if 6<=n<=20:
            print("Weird")
        if n>20:
            print("Not Weird")
if __name__ == '__main__':
    n = int(input().strip())
    check(n)
