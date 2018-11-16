from secret import flag
from Crypto.Util.number import *

assert flag.startswith('flag{')
assert flag.endswith('}')
pt = int(flag[5:-1].encode('hex'),16)
p = getPrime(30)
q = getPrime(25)
n = p*q
e = 65537
assert pt < n

print 'e:',e
print 'n:',n
print 'ct:',pow(pt,e,n)
