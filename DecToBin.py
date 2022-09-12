# take the input and parse it as an integer
inp = int(input())

# find the amount of bits needed
count, bitCount, val, bits, values = 0, 0, 1, [], []
while count < inp:
    bits.append(0)
    values.append(val)

    count = count + val
    val *= 2

# calculate the binary string
i = 0
for value in values[::-1]:
    # if next one is more than the desired value
    if value * 2 > inp and inp - value >= 0:
        bits[i] = 1
        inp -= value

    i += 1

# print the output
print("".join(map(str, bits)))
