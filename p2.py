str1 = raw_input("Input String 1 \n").decode("hex")
str2 = raw_input("Input Sting 2 \n" ).decode("hex")

xor = ""

for ch1, ch2 in zip(str1, str2):
    xor += chr(ord(ch1) ^ ord(ch2))

print(xor)
