from secret import flag
from Crypto.Util.number import *

assert len(flag)<20
pt = int(flag.encode('hex'),16)
p = getPrime(1024)
q = getPrime(1024)
n = p*q
e = 3
assert pt < n

print 'e:',e
print 'n:',n
print 'ct:',pow(pt,e,n)
