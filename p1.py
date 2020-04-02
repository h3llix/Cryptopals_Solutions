import base64

text = raw_input("Input String\n")
text = text.decode('hex')

encoded_b64 = base64.b64encode(text)

print encoded_b64
