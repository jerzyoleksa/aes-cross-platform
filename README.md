# aes-cross-platform
AES encryption and decryption in JavaScript, Java and Python

Verify if you get the same encryption output as with this online tool <br/>
https://www.devglan.com/online-tools/aes-encryption-decryption

<br/>
Pkcs5 padding is defined for 8-byte block sizes, Pkcs7 padding would work for any block size from 1 to 255 bytes<br/>
Java does not support Pkcs7, therefore an external security manager is required (ex. Bouncy Castle)
<br/><br/>
In Java specification, any Java distribution must implement just 2 padding types: NoPadding and Pkcs5<br/>
By the way Pkcs standard is much broader security package and padding is just a minor subset of it
<br/><br/>
```Java
package com.garnizon.encrypt.aes;
     
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
	    //Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
	    Cipher cipher = Cipher.getInstance("AES/ECB/PKCS7Padding", "BC");
	    SecretKey secretKey = new SecretKeySpec(keyBytes, "AES");
	    cipher.init(Cipher.DECRYPT_MODE, secretKey);
	    return cipher.doFinal(encryptedMessage);
	}	
	
	
  public static void main(String[] args) throws Exception {
    Security.addProvider(new org.bouncycastle.jce.provider.BouncyCastleProvider());    
    
    String encryptionKeyString =  "secret#456!23key";
    byte[] originalMessageBytes = "my secret data".getBytes();
    byte[] encryptionKeyBytes = encryptionKeyString.getBytes();
    
    byte[] cipherText = encryptMessage(originalMessageBytes, encryptionKeyBytes);
    System.out.println(new String(Base64.getEncoder().encode(cipherText)));
  }
  
}
        
```
