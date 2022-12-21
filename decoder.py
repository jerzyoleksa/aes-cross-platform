from Crypto.Cipher import AES
from pkcs7 import PKCS7Encoder
import pkcs7,threading, base64

key = 'administrational'
keyEnc = key.encode("utf8")

#1 message hardcoded
#enc_cipher = 'lbkY4V41z2IDY+zvEco69Q=='.encode("utf8")

#2 message from file
with open('encrypted.txt', 'r') as file:
    data = file.read()
enc_cipher = data.encode("utf8")
#end of file read

keyEnc = key.encode("utf8")

decodetext =  base64.b64decode(enc_cipher)

aes = AES.new(keyEnc, AES.MODE_ECB)
cipher = aes.decrypt(decodetext)
cipherDec = cipher.decode("utf8")

print(cipherDec)
