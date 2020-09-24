# Problem: https://open.kattis.com/problems/flexible
# Author: Cian Kehoe
# Submitted: September 24th, 2020

# process input
maxN = input().split()[0]
partitions = [int(n) for n in input().split()]

# add boundary values to partition array
partitions.append(int(maxN))
partitions.insert(0, 0)

# map to store all possible partition sizes
calc = {}

for i, v in enumerate(partitions):
    for i in partitions:
        size = (i - v)
        if size > 0:
            calc[size] = True

output = ([n for n in sorted(calc.keys())])

print(*output)