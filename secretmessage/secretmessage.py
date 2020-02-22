import math
import sys

num_messages = int(input())

for message in sys.stdin:
    message = message.strip('\n')
    L = len(message)
    # M --> smallest square number greater than or equal to L
    M = 0
    i = 1
    while M < L:
        M = i * i
        i += 1

    num_asterisks = M - L
    message = message + ("*" * num_asterisks)

    K = int(math.sqrt(M))

    output = ""

    j = 1
    while j <= K:
        # add each Kth character of message to output
        # reverse them
        # Ex. iloveyoutooJill* -> "ieti" -> "itei"
        output = output + message[::K][::-1]

        # remove first character from message each time
        # allows us to get next set of Kth characters
        message = message[1:]
        j += 1

    print(output.replace("*", ""))