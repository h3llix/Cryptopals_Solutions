from letter_frequency import letterFrequency
text = raw_input("Input Sting to decrypt \n")
text = text.decode("hex")
decoded = []  # initializing  list to store all strings xorred from values 0 to 255
temp = ""

for a in range(256):
    temp = ''.join([chr(ord(ch) ^ a) for ch in text])  # temp to store xorred string from each bit
    decoded.append(temp)
    temp = ""

scores = []  # list to store scores of each string in decoded
out = map(lambda x: x.upper(), decoded) # Iterate over each character and make each character uppercase

output = list(out)

for case in output:
    scores.append(sum(letterFrequency.get(ch, 0) for ch in case))

sorted_list = sorted(((v, i) for i, v in enumerate(scores)), reverse=True) #sort list according to their scores

for i in sorted_list[:10]:    #listing top 10 strings according to top scores
    x = tuple(i)
    print decoded[x[1]]
