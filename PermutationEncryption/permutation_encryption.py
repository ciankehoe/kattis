# Problem: https://open.kattis.com/problems/permutationencryption
# Author: Cian Kehoe
# Submitted: September 24th, 2020


while True:
    line = input()

    if line == "0":
        break

    # store key in array, key of size N
    key = line.strip().split(" ")[1:]
    N = len(key)

    # get input message
    msg = input()

    # pad the input if required
    if (len(msg) % N) != 0:
        padding_size = N - (len(msg) % N)
        msg = msg + (" " * padding_size)

    # process message
    # split message into array of slices of size N
    sliced_msg = [msg[i:i+N] for i in range(0, len(msg), N)]

    # store mapping of original position of 
    # each letter in slice.
    mapping = {}
    for idx, subslice in enumerate(sliced_msg):
        for i, c in enumerate(subslice):
            mapping[i] = c

        subslice = list(subslice)

        # encrypt message
        for k, v in mapping.items():
            swap_index = int(key[k]) - 1
            subslice[k] = mapping[swap_index]

        sliced_msg[idx] = subslice

    result = "".join(["".join(s) for s in sliced_msg])
    print(f"'{result}'")