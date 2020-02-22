num_temps = int(input())

print(len([int(temp) for temp in input().strip('\n').split() if int(temp) < 0]))
