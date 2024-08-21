from Crypto.Util.number import *

def chocolate_generator(m: int) -> int:
    p = 396430433566694153228963024068183195900644000015629930982017434859080008533624204265038366113052353086248115602503012179807206251960510130759852727353283868788493357310003786807
    return (pow(13, m, p) + pow(37, m, p)) % p

# Provided chocolate values
remain = [
    88952575866827947965983024351948428571644045481852955585307229868427303211803239917835211249629755846575548754617810635567272526061976590304647326424871380247801316189016325247,
    67077340815509559968966395605991498895734870241569147039932716484176494534953008553337442440573747593113271897771706973941604973691227887232994456813209749283078720189994152242
]

# Brute-force to find the golden ticket
golden_ticket = None
max_range = 2**24  # Increase the range even more

for m in range(max_range):
    if chocolate_generator(m) == remain[-1]:
        golden_ticket = m
        print(f"Golden ticket found: {golden_ticket}")
        break

if golden_ticket is not None:
    # Convert the golden ticket (integer) back to bytes to get the flag
    flag = long_to_bytes(golden_ticket)
    print(f"The flag is: {flag}")
else:
    print("Golden ticket not found within the given range.")
