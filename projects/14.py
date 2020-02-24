"""Problem 14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million."""


longest_chain = 0
known_lengths = {}
stating_num = 0

for i in range(1, 1000000):
    num = i
    chain_len = 1

    while num != 1:
        # keep track of known chain lengths for each number, so as not to have to recalculate them
        if num in known_lengths:
            chain_len += known_lengths[num]
            break

        if num % 2 == 0:
            num /= 2

        else:
            num = (3 * num) + 1

        chain_len += 1

    # store chain length of starting num
    known_lengths[i] = chain_len

    if chain_len > longest_chain:
        longest_chain = chain_len
        stating_num = i

print(stating_num)
