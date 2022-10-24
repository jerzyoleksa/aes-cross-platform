from Crypto.Cipher import AES
from pkcs7 import PKCS7Encoder
import pkcs7,threading, base64

key = 'secret#456!23key'
keyEnc = key.encode("utf8")

enc_cipher = 'lbkY4V41z2IDY+zvEco69Q=='.encode("utf8");
keyEnc = key.encode("utf8")

decodetext =  base64.b64decode(enc_cipher)

aes = AES.new(keyEnc, AES.MODE_ECB)
cipher = aes.decrypt(decodetext)
cipherDec = cipher.decode("utf8")

print(cipherDec)
