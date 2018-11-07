from secret import flag
import random
from Crypto.Util.number import *

pt = int(flag.encode('hex'),16)
p = getPrime(1024)
q = getPrime(1024)
n = p*q
d = random.randrange(0,2**256)
e = inverse(d, (p-1)*(q-1))
assert pt < n

print 'e:',e
print 'n:',n
print 'ct:',pow(pt,e,n)
