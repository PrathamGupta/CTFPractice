# Transformation

Challenge in Reverse Engineering

### Given :

In this challenge we are given a file named "enc".

### Examination : 

We can read this file using:

```bash
cat  enc
```

We see that the output of the same is:

```
灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥㜰㍢㐸㙽
```

### Methods:

- I tried first using cyberchef but could not view any sort of results, Magic showed me that the UTF8 kind of decoding should be used but the flag I got from it was not the answer and hence I think I did not get enough from it. 
- Next method we can use is to decode it myself using a python script. 

### Answer: 

In the python script, we first read the input and then create a flag variable. 

After the flag variable is created we iterate over the encoded flag and then convert the ord of the character to 8 bit and then decode it into utf-16. We then join the two and find our flag, the hint is given in the question itself. 

The answer for this challenge is: 

<details>
  <summary>Spoiler warning</summary>
  
  ```
  picoCTF{16_bits_inst34d_of_8_e703b486}
  ```
  
</details>
