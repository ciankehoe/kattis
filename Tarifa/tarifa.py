X = int(input())

N = int(input())

total_available = X

i = 0
while i < N:
    P = int(input())
    total_available += (X - P)
    i += 1

print(total_available)