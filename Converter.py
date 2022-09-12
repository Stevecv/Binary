def askChoice(inp):
    choice = input("Choose: \n1. Decimal to Binary \n2. Binary to Decimal\n")
    if choice == "1":
        print(decToBin(inp))
    elif choice == "2":
        print(binToDec(inp))
    else:
        print("You can only chose 1 or 2!")
        askChoice()


       
def decToBin(inp):
    # take the input and parse it as an integer
    inp = int(inp)

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
    return "".join(map(str, bits))


def binToDec(inp):
    value = 1
    out = 0
    for byte in reversed(inp):
        if byte == "1":
            out = out+value

        value = value*2
    return out



inp = input("Enter your value > ")
if "2" in inp or "3" in inp or "4" in inp or "5" in inp or "6" in inp or "7" in inp or "8" in inp or "9" in inp:
    #Has to be a denary number
    print(decToBin(inp))

else:
    askChoice(inp)
