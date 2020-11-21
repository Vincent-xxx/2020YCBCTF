

# This file was *autogenerated* from the file ./exp.sage
from sage.all_cmdline import *   # import sage library

_sage_const_1521743372908865262741416546733910591548610853500085844733002429309461943187859390289514438469431138029742327155080552292148353482583527260905036928681873676910590690604515369082156097890991972036529002074379125852781768163227840719208682860171159807675102132598520553630516018243653510522481924736453744019712183046155976913571639072382518649897680681556092056484077209628330583478716242389217196014744971281141813768285089065970771971055297965442402683859945510279083854176013322215977145866415466285406978295676624195169518720793348311237519665991770047537451030866696493474098850568929871361771005057843597772734669939 = Integer(1521743372908865262741416546733910591548610853500085844733002429309461943187859390289514438469431138029742327155080552292148353482583527260905036928681873676910590690604515369082156097890991972036529002074379125852781768163227840719208682860171159807675102132598520553630516018243653510522481924736453744019712183046155976913571639072382518649897680681556092056484077209628330583478716242389217196014744971281141813768285089065970771971055297965442402683859945510279083854176013322215977145866415466285406978295676624195169518720793348311237519665991770047537451030866696493474098850568929871361771005057843597772734669939); _sage_const_21 = Integer(21); _sage_const_8 = Integer(8); _sage_const_1024 = Integer(1024); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0)
from sage.all import *

n = _sage_const_1521743372908865262741416546733910591548610853500085844733002429309461943187859390289514438469431138029742327155080552292148353482583527260905036928681873676910590690604515369082156097890991972036529002074379125852781768163227840719208682860171159807675102132598520553630516018243653510522481924736453744019712183046155976913571639072382518649897680681556092056484077209628330583478716242389217196014744971281141813768285089065970771971055297965442402683859945510279083854176013322215977145866415466285406978295676624195169518720793348311237519665991770047537451030866696493474098850568929871361771005057843597772734669939 

pattern_size = _sage_const_21 *_sage_const_8 
prime_size = _sage_const_1024 
x = _sage_const_2 **pattern_size
d0 = _sage_const_2 **pattern_size - _sage_const_1 
w = _sage_const_2 **prime_size
u, v = divmod(n, w)
M = matrix([[x, _sage_const_0 , u * d0 % w],
            [_sage_const_0 , x, v * d0 % w],
            [_sage_const_0 , _sage_const_0 ,         w]])

for vec in M.LLL():
  bx, ax = vec[_sage_const_0 ], -vec[_sage_const_1 ]
  p = gcd(ax * w + bx, n)
  if _sage_const_1  < p < n:
    q = n // p
    break

print(p)
print(q)


