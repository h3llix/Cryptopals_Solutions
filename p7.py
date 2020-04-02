import base64
from Crypto.Cipher import AES

with open('7.txt') as file_in:
    line = base64.b64decode(file_in.read())

key = 'YELLOW SUBMARINE'

object_aes = AES.new(key, AES.MODE_ECB)
decryption = object_aes.decrypt(line)

print decryption
