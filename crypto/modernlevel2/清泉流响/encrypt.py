from secret import flag
import random
from Crypto.Util.number import *

pt = int(flag.encode('hex'),16)
p = getPrime(1024)
q = p+200
while not isPrime(q):
    q += 1
n = p*q
e = 65537
assert pt < n

print 'e:',e
print 'n:',n
print 'ct:',pow(pt,e,n)
