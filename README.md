# aes-cross-platform
AES encryption and decryption in JavaScript, Java and Python

Verify if you get the same encryption output as with this online tool <br/>
https://www.devglan.com/online-tools/aes-encryption-decryption

<br/><br/>
<b>Java</b>
<br/>
Pkcs5 padding is defined for 8-byte block sizes, Pkcs7 padding would work for any block size from 1 to 255 bytes<br/>
Java does not support Pkcs7, therefore an external security manager is required (ex. Bouncy Castle)
<br/><br/>
In Java specification, any Java distribution must implement just 2 padding types: NoPadding and Pkcs5<br/>
By the way Pkcs standard is much broader security package and padding is just a minor subset of it
<br/><br/>

> In order to use Bouncy Castle as the security provider, you can either change the java.policy file in your JVM (and its the hard way),
> or you can use the <b>signed jar</b> file provided by the Bouncy Castle on their website (it was <b>bcprov-jdk15to18-172.jar</b> in my case).
> https://www.bouncycastle.org/download/bcprov-jdk15to18-172.jar

```java	
import java.security.Security;
import java.util.Base64;
import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;

public class DecryptBC {

	public static byte[] encryptMessage(byte[] message, byte[] keyBytes) throws Exception {
		Cipher cipher = Cipher.getInstance("AES/ECB/PKCS7Padding", "BC");
		SecretKey secretKey = new SecretKeySpec(keyBytes, "AES");
		cipher.init(Cipher.ENCRYPT_MODE, secretKey);
		return cipher.doFinal(message);
	}

	public static byte[] decryptMessage(byte[] encryptedMessage, byte[] keyBytes) throws Exception {
		// Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
		Cipher cipher = Cipher.getInstance("AES/ECB/PKCS7Padding", "BC");
		SecretKey secretKey = new SecretKeySpec(keyBytes, "AES");
		cipher.init(Cipher.DECRYPT_MODE, secretKey);
		return cipher.doFinal(encryptedMessage);
	}

	public static void main(String[] args) throws Exception {
		Security.addProvider(new org.bouncycastle.jce.provider.BouncyCastleProvider());

		String encryptionKeyString = "secret#456!23key";
		byte[] originalMessageBytes = "my secret data".getBytes();
		byte[] encryptionKeyBytes = encryptionKeyString.getBytes();

		byte[] cipherText = encryptMessage(originalMessageBytes, encryptionKeyBytes);
		System.out.println("encryption output:"+new String(Base64.getEncoder().encode(cipherText)));
		System.out.println("decrypted output:"+new String(decryptMessage(cipherText, encryptionKeyBytes)));
	}

}
```


<br/><br/>
<b>Python</b>
<br/>

```python	
from Crypto.Cipher import AES
from pkcs7 import PKCS7Encoder
import pkcs7,threading, base64


text='my secret data'
key = 'secret#456!23key'

#TypeError: Object type <class 'str'> cannot be passed to C code
#In Python 3, encode it into a bytearray:

keyEnc = key.encode("utf8")
textEnc = text.encode("utf8")

aes = AES.new(keyEnc, AES.MODE_ECB)

#PKCS7Encoder doesnt work with strings
encoder = PKCS7Encoder()
pad_text = encoder.encode(text)
pad_textEnc = pad_text.encode("utf8")

print('text:' + text)
print('pad_text:', pad_text)
print('pad_textEnc:', pad_textEnc)

cipher = aes.encrypt(pad_textEnc)
enc_cipher = base64.b64encode(cipher)

print('cipher:', cipher)
print('enc_cipher:', enc_cipher)

decodetext =  base64.b64decode(enc_cipher)

aes = AES.new(keyEnc, AES.MODE_ECB)
cipher = aes.decrypt(decodetext)
print(cipher)

cipherDec = cipher.decode("utf8")

pad_text = encoder.decode(cipherDec)
print(pad_text)
```


<br/><br/>
<b>JavaScript</b>
<br/>

```javascript
import CryptoJS from "crypto-js";

let key = 'secret#456!23key' //(16 Byte key for 128 Bit AES)

const decryptWithAES = (ciphertext) => {
  const bytes = CryptoJS.AES.decrypt(ciphertext, CryptoJS.enc.Utf8.parse(key), {
    mode: CryptoJS.mode.ECB,
    padding: CryptoJS.pad.Pkcs7
  });
  return bytes.toString(CryptoJS.enc.Utf8);
}

const encryptTextWithAES = (plaintText) => {
  const encryptedData = CryptoJS.AES.encrypt(plaintText, CryptoJS.enc.Utf8.parse(key), {
    mode: CryptoJS.mode.ECB,
    padding: CryptoJS.pad.Pkcs7
  });
  return encryptedData.toString();    
}

export {encryptTextWithAES, decryptWithAES}
```
