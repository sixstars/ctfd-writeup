from secret import flag
import random
from Crypto.Util.number import *

pt = int(flag.encode('hex'),16)
p = getPrime(2048)
q = getPrime(2048)
n = p*q
e1 = 65537
e2 = 988727
assert pt < n

print 'e1:',e1
print 'e2:',e2
print 'n:',n
print 'ct1:',pow(pt,e1,n)
print 'ct2:',pow(pt,e2,n)
