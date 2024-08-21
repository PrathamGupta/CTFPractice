## This is the answer for Crypto challenge Golden Ticket from the offcial idek CTF github
## https://github.com/idekctf/idekctf-2024/blob/main/crypto/goldenticket/debug/solve.py

from sage.all import discrete_log_lambda, CRT, lcm, GF
from Crypto.Util.number import *

def PH_partial(h, g, p, fact_phi):
    """Returns (x, m), where
    - x is the dlog of h in base g, mod m
    - m = lcm(pi^ei) for (pi, ei) in fact_phi
    """
    res = []
    mod = []
    F = GF(p)

    phi = p-1
    for pi, ei in fact_phi:
        gi = pow(g, phi//(pi**ei), p)
        hi = pow(h, phi//(pi**ei), p)
        xi = discrete_log_lambda(F(hi), F(gi), bounds = (0, pi**ei))
        res.append(int(xi))
        mod.append(int(pi**ei))

    x, m = CRT(res, mod), lcm(mod)
    assert pow(g, x * phi//m, p) == pow(h, phi//m, p)
    return x, m

# x = 13^(g-1) + 37^(g-1)
# y = 13^g + 37^g
# 37*x - y = 37*13^(g-1) - 13^g
#          = 13^(g-1)*(37-13)


## Here p is given to us in the source code of the original challenge
## And we see that x and y are the values which are present in the remain part of the code 
p = 396430433566694153228963024068183195900644000015629930982017434859080008533624204265038366113052353086248115602503012179807206251960510130759852727353283868788493357310003786807
x,y = [88952575866827947965983024351948428571644045481852955585307229868427303211803239917835211249629755846575548754617810635567272526061976590304647326424871380247801316189016325247, 67077340815509559968966395605991498895734870241569147039932716484176494534953008553337442440573747593113271897771706973941604973691227887232994456813209749283078720189994152242]

# from factordb
fs = [2, 530897, 550513, 578483, 579757, 596977, 605837, 606173, 608389, 631483, 632501, 663907, 674357, 742607, 749051, 763597, 790817, 813797, 824683, 832291, 845753, 856343, 880531, 885061, 899177, 899321, 942187, 972637, 1014149, 1031347, 1032901]
fs = [(e,1) for e in fs]

h = 13 * pow(37-13, -1, p) * (37*x - y) % p # h = 13^g
g, m = PH_partial(h, 13, p, fs)
print('g =', g)

print(long_to_bytes(g))