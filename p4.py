from letter_frequency import letterFrequency

lines = []  # list to store all lines in the given text file

with open("4.txt") as file_in:
    for line in file_in:
        lines.append(line.strip())


def single_xor(text):
    text = text.decode("hex")
    decoded = []
    for a in range(256):
        temp = ''.join([chr(ord(ch) ^ a) for ch in text])
        decoded.append(temp)
        temp = ""
    return decoded


def calculate_score(decoded1):
    scores = []  # list to stores scores according to frequency of charecter
    scores1 = [] #
    out = map(lambda x: x.upper(), decoded1)  # converting each letter to upper
    output = list(out)

    for case in output:
        scores.append(sum(letterFrequency.get(ch, 0) for ch in case))

    sorted_list = sorted(((v, i) for i, v in enumerate(scores)), reverse=True) # sorting scores from max to min and enumerating them to store the index of
    for i in sorted_list:
        scores1.append(i)
    return max(scores1) #returning max of score


ekdum_final = []
finalscore = [] #storing max scores of all the lines    1

for line in lines:
    finalscore.append(calculate_score(single_xor(line)))

sorted_mylist1 = sorted(((v, i) for i, v in enumerate(finalscore)), reverse=True)

for i in sorted_mylist1:
    x = tuple(i)
    print(x)

string = "Now you see the output as ((x,y),z) where z is the line in the given text file having highest score x and if we single decipher line z with bit  y is having the max score"
print string
x = int(raw_input("NOw you have seen it enter which line you want to decipher"))
anss = single_xor(lines[x])
y = int(raw_input("you chose line {} now enter which bit to xor it with ".format(x)))
for ans in anss[y:y + 1]:
    print ans
