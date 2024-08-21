# Golden Ticket

Challenge in Cryptography

## Given :

In this challenge we are given a file named "chall.py" which is here in the repository called "challenge.py". That is all that we are given and nothing more. 

## Methods:

- I tried understanding the question but did not understand it, but then I tried ChatGPT and it also did not help. But I understood one thing that the challenge required me to break the mathematical equation it was forming in the code. 
- After the ctf ended, I found the solution and will try to understand it here. 
- The solution can be found in solve.py 

## Examination of source code: 

We see that we have a function named "chocolate_generator":

```python
def chocolate_generator(m: int) -> int:
    p = 396430433566694153228963024068183195900644000015629930982017434859080008533624204265038366113052353086248115602503012179807206251960510130759852727353283868788493357310003786807
    return (pow(13, m, p) + pow(37, m, p)) % p
```

Here we can see that there is a value known as p which is being returned with a mathematical expression. The mathematical equation would be 

$$ (13^m\ \%\ p\ +\ 37^m\ \%\ p)\ \%\ p $$

Now the next part of the code we see that the flag is being hidden inside of the golden ticket. 

```python
flag = b"idek{REDACTED}"
golden_ticket = bytes_to_long(flag)
flag_chocolate = chocolate_generator(golden_ticket)
```

Now in this part of the code, we see that the flag is being generated and then converted to long using bytes_to_long and then sent to the function that we previously saw and stored in the flag_chocolate variable. 

```python
chocolate_bag = []

for i in range(golden_ticket):
    chocolate_bag.append(chocolate_generator(i))

chocolate_bag.append(flag_chocolate)
```

Now after this we see that each number till the golden ticket has been sent to the same function and then the value is stored in the chocolate bag. 

```python
remain = chocolate_bag[-2:]
print(remain)
```

Now all of the values except the last two are deleted and we are given those values to determine the original flag for getting the golden ticket. 

Fortunately for us, we do not need to run the code for a long time as in the final comment we find the values of the last two remaining chocolates. 

```python 
[88952575866827947965983024351948428571644045481852955585307229868427303211803239917835211249629755846575548754617810635567272526061976590304647326424871380247801316189016325247, 67077340815509559968966395605991498895734870241569147039932716484176494534953008553337442440573747593113271897771706973941604973691227887232994456813209749283078720189994152242]
```

## Explanation of the Answer:

The basis of the answer depends on the mathematical equations. 

Let g be our flag which is used in the last mathematical function, x be our second last value without the mod p and y be our last value without mod p. Then, 

$$ x\ =\ 13^{(g-1)}\ +\ 37^{(g-1)}$$
$$ y\ =\ 13^{g}\ +\ 37^{g}$$

Then we can use basic maths to see, 

$$ 37*x\ -\ y\ =\ 37*13^{(g-1)}\ -\ 13^g $$

Which can be written as, 

$$ 37*x\ -\ y\ =\ 13^{(g-1)} *(37-13)$$

Now if we just solve for g with the values we know of x and y, then we can find the flag. 

The hard part here for me was how to find the solution of the equation to solve for g, as the answer would require the use of log base 13 and I have not that much experience coding mathematical equations. 

So the solution then provides the way of deducing this mathematical formula using python code. 

## Answer: 

The answer for this challenge is: 

<details>
  <summary>Spoiler warning</summary>
  
  ```
  idek{charles_and_the_chocolate_factory!!!}
  ```
  
</details>
