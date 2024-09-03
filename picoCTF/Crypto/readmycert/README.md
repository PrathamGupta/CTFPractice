# Iterencdec

Challenge in Cryptography

### Given :

In this challenge we are given a file named "enc_flag".

### Examination : 

We can read this file using:

```bash
cat  enc_flag
```

We see that the output of the same is:

```
YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclh6YzRNalV3YUcxcWZRPT0nCg==
```

### Methods:

- This question was very easy as we can see that the value is base64 and we can use online tools to decrypt it 
- The interesting part of the answer is that the answer to the decrypted value is also in base64, so we have to do the decryption again 
- After the two decryption from base64, we can see that the value is still encrypted but we can see that the pattern matches that of ROT13 so we use that to decrypt and we find the flag

### Answer: 

openssl req -in mycsr.csr -noout -text

The answer for this challenge is: 

<details>
  <summary>Spoiler warning</summary>
  
  ```
  picoCTF{read_mycert_693f7c03}
  ```
  
</details>
