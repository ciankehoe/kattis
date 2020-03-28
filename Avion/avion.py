CIA_blimps = []

for i in range(5):
    reg = input().strip("\n")
    if "FBI" in reg:
        CIA_blimps.append(i + 1)

if len(CIA_blimps) > 0:
    print(*CIA_blimps)
else:
    print("HE GOT AWAY!")