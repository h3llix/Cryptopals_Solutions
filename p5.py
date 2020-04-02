def multikey_xor(text, key):
    temp = ""
    index = 0
    for i in text:
        temp += chr(ord(i) ^ ord(key[index]))
        if (index == len(key) - 1):   #when index reaches length of key reset index to zero
            index = 0

        else:
            index += 1
    return temp


text = "Burning 'em, if you ain't quick and nimble \n I go crazy when I hear a cymbal"
key = "ICE"

ans = multikey_xor(text, key)
print(ans)

