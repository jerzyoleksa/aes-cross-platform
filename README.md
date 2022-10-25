# aes-cross-platform
AES encryption and decryption in JavaScript, Java and Python

Verify if you get the same encryption output as with this online tool <br/>
https://www.devglan.com/online-tools/aes-encryption-decryption

<br/>
Pkcs5 padding is defined for 8-byte block sizes, Pkcs7 padding would work for any block size from 1 to 255 bytes
Java does not support Pkcs7, therefore an external security manager is required (ex. Bouncy Castle)
In Java specification, any Java distribution must implement just 2 padding types: NoPadding and Pkcs5
By the way Pkcs standard is much broader security package and padding is just a minor subset of it
