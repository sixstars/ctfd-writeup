from secret import flag
import random
from Crypto.Util.number import *

pt = int(flag.encode('hex'),16)
p = getPrime(2048)
q = getPrime(2048)
n = p*q
e = 65537
e0 = getPrime(233)
d0 = inverse(e0, (p-1)*(q-1))

assert pt < n

print 'pair:',(e0,d0)
print 'e:',e
print 'n:',n
print 'ct:',pow(pt,e,n)
