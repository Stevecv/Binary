value = 1
out = 0
for byte in reversed(input()):
    if byte == "1":
        out = out+value

    value = value*2
print(out)
