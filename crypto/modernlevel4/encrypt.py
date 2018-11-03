from secret import flag
import random
from Crypto.Util.number import *

pt = int(flag.encode('hex'),16)
p = getPrime(2048)
q1 = getPrime(2048)
q2 = getPrime(2048)
if q1 > q2:
    q1, q2 = q2, q1
n1 = p*q1
n2 = p*q2
e = 65537
assert pt < n1

print 'e:',e
print 'n1:',n1
print 'n2:',n2
print 'ct:',pow(pow(pt,e,n1),e,n2)
