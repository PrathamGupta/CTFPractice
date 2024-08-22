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

The command used for decrypting from base64 is 

```bash
echo "YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclh6YzRNalV3YUcxcWZRPT0nCg==" | base64 -d
```

The answer to this would be:

```bash
b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzc4MjUwaG1qfQ=='
```

The next step would be to do:

```bash
echo "d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzc4MjUwaG1qfQ==" | base64 -d
```

The answer to this would be:

```bash
wpjvJAM{jhlzhy_k3jy9wa3k_78250hmj}%
```

The next step would be to do:

```bash
echo "wpjvJAM{jhlzhy_k3jy9wa3k_78250hmj}" | tr 'A-Za-z' 'T-ZA-St-za-s'
```

The answer for this challenge is: 

<details>
  <summary>Spoiler warning</summary>
  
  ```
  picoCTF{16_bits_inst34d_of_8_e703b486}
  ```
  
</details>
