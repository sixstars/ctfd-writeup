from secret import flag
import random
from Crypto.Util.number import *

pt = int(flag.encode('hex'),16)
p = getPrime(1024)
q = getPrime(1024)
n = p*q
e = 3 # just save time
d = inverse(e, (p-1)*(q-1))
d0 = d&((2**800)-1)
assert pt < n

print 'e:',e
print 'partial d:', d0
print 'n:',n
print 'ct:',pow(pt,e,n)
