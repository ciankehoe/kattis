# Problem: https://open.kattis.com/problems/nodup
# Author: Cian Kehoe
# Submitted: September 24th, 2020

import sys

def solution1():
    line = input().split()
    dups = dict()

    for word in line:
        if word in dups:
            print("no")
            sys.exit()
        else:
            dups[word] = True
    print("yes")


def solution2():
    line = input().split()
    if len(line) == len(set(line)):
        print("yes")
    else:
        print("no")


if __name__ == "__main__":
    solution2()