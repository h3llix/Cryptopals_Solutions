lines=[]
with open('8.txt') as file_in:
    for line in file_in:
        lines.append(bytearray(line.strip().decode("hex")))

print lines[0]
